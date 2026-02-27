import streamlit as st
import requests
import uuid

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Internal Chatbot")

if "access_token" not in st.session_state:
    st.session_state.access_token = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

def login():
    # Remove excessive top padding and expand max width for a desktop-friendly layout
    st.markdown("""
        <style>
        .block-container {
            padding-top: 4rem;
            padding-bottom: 0rem;
            max-width: 950px !important;
        }
        /* Custom styling for the form */
        [data-testid="stForm"] {
            border-radius: 16px;
            padding: 2.5rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            border: 1px solid #F3F4F6;
            background-color: #FFFFFF;
        }
        /* Override Streamlit's primary button to our indigo color */
        button[kind="primary"] {
            background-color: #4F46E5 !important;
            border-color: #4F46E5 !important;
            color: white !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }
        button[kind="primary"]:hover {
            background-color: #4338CA !important;
            border-color: #4338CA !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Use a split-screen layout well suited for laptops/PCs
    st.markdown("<br>", unsafe_allow_html=True)
    col1, spacing, col2 = st.columns([1.1, 0.1, 1])
    
    with col1:
        st.markdown("<h1 style='color: #111827; font-size: 3.2rem; line-height: 1.2; margin-bottom: 1rem; margin-top: 1rem;'>Internal<br><span style='color: #4F46E5;'>AI Chatbot</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #4B5563; font-size: 1.15rem; line-height: 1.6; margin-bottom: 2rem;'>Your intelligent workplace assistant. Access customized knowledge, automate tasks, and get instant answers securely.</p>", unsafe_allow_html=True)
        
        # Add some nice list items
        st.markdown("""
        <div style='display: flex; flex-direction: column; gap: 1rem;'>
            <div style='display: flex; align-items: center; gap: 1rem;'>
                <div style='background-color: #EEF2FF; color: #4F46E5; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;'>🔒</div>
                <span style='color: #374151; font-weight: 500; font-size: 1.05rem;'>Secure & Private Access</span>
            </div>
            <div style='display: flex; align-items: center; gap: 1rem;'>
                <div style='background-color: #EEF2FF; color: #4F46E5; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;'>⚡</div>
                <span style='color: #374151; font-weight: 500; font-size: 1.05rem;'>Instant Intelligent Answers</span>
            </div>
            <div style='display: flex; align-items: center; gap: 1rem;'>
                <div style='background-color: #EEF2FF; color: #4F46E5; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;'>📚</div>
                <span style='color: #374151; font-weight: 500; font-size: 1.05rem;'>Company Knowledge Base</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        with st.form("login_form", clear_on_submit=False):
            st.markdown("<h3 style='color: #111827; margin-bottom: 0.5rem;'>Welcome Back</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color: #6B7280; font-size: 0.95rem; margin-bottom: 1.5rem;'>Sign in to your account to continue</p>", unsafe_allow_html=True)
            
            username = st.text_input("Work Email", placeholder="name@company.com")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("Sign In →", type="primary", use_container_width=True)

            if submit:
                if not username or not password:
                    st.warning("⚠️ Please provide both a username and password.")
                else:
                    try:
                        with st.spinner("Signing in..."):
                            response = requests.post(f"{API_URL}/login", data={"username": username, "password": password})
                            if response.status_code == 200:
                                data = response.json()
                                st.session_state.access_token = data.get("access_token")
                                st.success("✅ Login successful! Redirecting...")
                                st.rerun()
                            else:
                                st.error("❌ Invalid username or password.")
                    except Exception as e:
                        st.error(f"❌ Failed to connect to backend API.")

def logout():
    st.session_state.access_token = None
    st.session_state.messages = []
    st.session_state.conversation_id = str(uuid.uuid4())
    st.rerun()

def chat_interface():
    # Inject custom CSS for the chat interface
    st.markdown("""
        <style>
        /* Set max width for the chat container to make it readable */
        .block-container {
            max-width: 900px !important;
            padding-top: 2rem;
        }
        /* User message bubble */
        [data-testid="stChatMessage"][aria-label="user message"] {
            background-color: #F8FAF8;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 1rem;
        }
        /* Assistant message bubble */
        [data-testid="stChatMessage"][aria-label="assistant message"] {
            background-color: #EEF2FF;
            border: 1px solid #C7D2FE;
            border-radius: 12px;
            padding: 1rem;
        }
        /* Sidebar custom styles */
        .sidebar-title {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #6B7280;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
            padding-left: 0.5rem;
        }
        .history-item {
            padding: 0.6rem 0.8rem;
            border-radius: 8px;
            color: #374151;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background-color: transparent;
            border: 1px solid transparent;
            transition: all 0.2s;
            margin-bottom: 0.25rem;
        }
        .history-item:hover {
            background-color: #F3F4F6;
            border-color: #E5E7EB;
        }
        .history-item-active {
            background-color: #EEF2FF;
            color: #4F46E5;
            font-weight: 500;
            border-color: #4F46E5;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("<h2 style='color: #111827; margin-bottom: 1.5rem;'>🤖 AI Assistant</h2>", unsafe_allow_html=True)
        
        if st.button("➕ New Chat", use_container_width=True, type="primary"):
            st.session_state.messages = []
            st.session_state.conversation_id = str(uuid.uuid4())
            st.rerun()
            
        st.markdown("<div class='sidebar-title'>Recent Chats</div>", unsafe_allow_html=True)
        
        # Display the current active chat session in the history section
        # Ideally, you would fetch historical conversation IDs from the backend here.
        # For now, we represent the current session dynamically.
        session_id_short = st.session_state.conversation_id[:8]
        if st.session_state.messages:
            preview = st.session_state.messages[0]["content"][:20] + "..."
        else:
            preview = "New Conversation"
            
        st.markdown(f"""
        <div class='history-item history-item-active'>
            💬 <span>{preview}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='sidebar-title'>Settings</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='padding-left: 0.5rem; color: #9CA3AF; font-size: 0.8rem;'>Session: {session_id_short}</p>", unsafe_allow_html=True)
        
        if st.button("🚪 Logout", use_container_width=True):
            logout()

    # Main chat header
    st.markdown("""
        <div style='border-bottom: 1px solid #E5E7EB; padding-bottom: 1rem; margin-bottom: 2rem;'>
            <h2 style='color: #1F2937; margin: 0;'>Internal Chatbot Workspace</h2>
            <p style='color: #6B7280; font-size: 0.95rem; margin: 0; margin-top: 0.25rem;'>Your private AI for instant knowledge retrieval</p>
        </div>
    """, unsafe_allow_html=True)

    # Display empty state if no messages
    if not st.session_state.messages:
        st.markdown("""
            <div style='text-align: center; padding: 4rem 0; color: #9CA3AF;'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>👋</div>
                <h3 style='color: #4B5563;'>How can I help you today?</h3>
                <p>Try asking a question about internal policies, projects, or specific documents.</p>
            </div>
        """, unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Message the chatbot..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

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
                with requests.post(f"{API_URL}/chat", json=payload, headers=headers, stream=True) as response:
                    if response.status_code == 200:
                        for chunk in response.iter_content(chunk_size=20, decode_unicode=True):
                            if chunk:
                                full_response += chunk
                                message_placeholder.markdown(full_response + "▌")
                        
                        message_placeholder.markdown(full_response)
                        
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
