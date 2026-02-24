import streamlit as st
import requests
import uuid
import json

# Configuration
API_URL = "http://localhost:8000"

st.set_page_config(page_title="Internal Chatbot", page_icon="🤖")

# Initialize session state
if "access_token" not in st.session_state:
    st.session_state.access_token = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

def login():
    st.title("Login to Internal Chatbot")
    with st.form("login_form"):
        username = st.text_input("Username (Email)")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            try:
                response = requests.post(f"{API_URL}/login", data={"username": username, "password": password})
                if response.status_code == 200:
                    data = response.json()
                    st.session_state.access_token = data.get("access_token")
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            except Exception as e:
                st.error(f"Failed to connect to backend API: {e}")

def logout():
    st.session_state.access_token = None
    st.session_state.messages = []
    st.session_state.conversation_id = str(uuid.uuid4())
    st.rerun()

def chat_interface():
    st.title("Internal Chatbot Assistant")
    
    # Sidebar for layout / actions
    with st.sidebar:
        st.header("Chat Controls")
        if st.button("New Chat"):
            st.session_state.messages = []
            st.session_state.conversation_id = str(uuid.uuid4())
            st.rerun()
        if st.button("Logout"):
            logout()
            
        st.caption(f"Conversation ID: {st.session_state.conversation_id[:8]}...")

    # Display chat history from session state
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Message the chatbot..."):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            headers = {
                "Authorization": f"Bearer {st.session_state.access_token}",
                "Content-Type": "application/json"
            }
            payload = {
                "query": prompt,
                "conversation_id": st.session_state.conversation_id
            }

            try:
                # Use streaming request
                with requests.post(f"{API_URL}/chat", json=payload, headers=headers, stream=True) as response:
                    if response.status_code == 200:
                        for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                            if chunk:
                                full_response += chunk
                                # Show current streamed text (adding a cursor to simulate typing)
                                message_placeholder.markdown(full_response + "▌")
                        
                        # Final response without cursor
                        message_placeholder.markdown(full_response)
                        
                        # Add to session state
                        st.session_state.messages.append({"role": "assistant", "content": full_response})
                    elif response.status_code == 401:
                        st.error("Session expired or invalid token. Please log in again.")
                        logout()
                    else:
                        st.error(f"Error: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect to backend API: {e}")

if st.session_state.access_token is None:
    login()
else:
    chat_interface()
