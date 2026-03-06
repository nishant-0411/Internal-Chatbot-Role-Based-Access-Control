const promptForm = document.querySelector('.prompt-form');
const promptInput = document.querySelector('.prompt-input');
const chatsContainer = document.querySelector('.chats-container');
const conatiner = document.querySelector('.container');
const fileInput = document.querySelector('#file-input');
const fileUploadWrapper = document.querySelector('.file-upload-wrapper');
// API Configuration
const API_BASE_URL = ['localhost', '127.0.0.1', '[::1]', '::1', '[::]', '::'].includes(window.location.hostname)
    ? 'http://127.0.0.1:8000'
    : window.location.origin;

// Auth Guard
const accessToken = localStorage.getItem('access_token');
if (!accessToken) {
    window.location.href = '../login page/login.html';
}

const userData = { messages: "", files: [] };
let userMessages = "";
const chatHistory = [];
const savedSessions = {}; // Store raw HTML snapshots of chats
let currentChatId = Date.now().toString(); // unique ID for active session

const createmessageElement = (messageHtml, ...messageType) => {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', ...messageType);
    messageDiv.innerHTML = messageHtml;
    return messageDiv;
}
const scrollToBottom = () => conatiner.scrollTo({
    top: conatiner.scrollHeight,
    behavior: "smooth"
});
const typingeffect = (text, textElement, chatbotmessageDiv) => {
    textElement.textContent = "";
    const word = text.split(" ");
    let index = 0;
    const interval = setInterval(() => {
        if (index < word.length) {
            textElement.textContent += word[index] + " ";
            index++;
            scrollToBottom();
        } else {
            clearInterval(interval);
            chatbotmessageDiv.classList.remove("loading");
        }
    }, 100);

}
const generateChatbotResponse = async (chatbotmessageDiv) => {
    const textElement = chatbotmessageDiv.querySelector(".message-text");

    chatHistory.push({
        role: "user",
        parts: [
            { text: userData.messages },
            ...userData.files.map(f => ({ inline_data: { data: f.data, mime_type: f.mime_type } }))
        ]
    });

    try {
        const payload = {
            query: userData.messages,
            conversation_id: currentChatId
        };

        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            },
            body: JSON.stringify(payload)
        });

        if (response.status === 401) {
            localStorage.removeItem('access_token');
            window.location.href = '../login page/login.html';
            return;
        }

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        chatbotmessageDiv.classList.remove("loading");
        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        let chatbotResponse = "";

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value, { stream: true });
            chatbotResponse += chunk;
            textElement.innerHTML = parseMarkdown(chatbotResponse.trimStart()) + "▌"; // simple blinker
            scrollToBottom();
        }

        // Final render without cursor
        textElement.innerHTML = parseMarkdown(chatbotResponse.trim());

        chatHistory.push({ role: "model", parts: [{ text: chatbotResponse }] });
        console.log("Chat History:", chatHistory);

    } catch (error) {
        console.error("Error generating chatbot response:", error);
        chatbotmessageDiv.classList.remove("loading");
        textElement.textContent = "Error connecting to the chatbot API.";
    } finally {
        userData.files = [];
    }
}

// Simple parsing for basic markdown (bold, italic, code). Add more if needed.
const parseMarkdown = (text) => {
    let result = text.replace(/\\n/g, '<br>'); // Newlines
    result = result.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>'); // Bold
    result = result.replace(/\*(.*?)\*/g, '<em>$1</em>'); // Italic
    result = result.replace(/`(.*?)`/g, '<code>$1</code>'); // Inline Code
    return result;
}
const handleformSubmit = (e) => {
    e.preventDefault();
    const userMessages = promptInput.value.trim();
    if (userMessages === "") return;

    // Hide Welcome Header when a chat starts
    const appHeader = document.querySelector(".app-header");
    if (appHeader && chatsContainer.children.length === 0) {
        appHeader.style.display = "none";
    }

    promptInput.value = "";
    userData.messages = userMessages;
    console.log(userMessages);
    const filesHtml = userData.files.map(file => {
        if (file.isImage) {
            return `<img src="data:${file.mime_type};base64,${file.data}" class="img-attachment" />`;
        } else {
            const ext = file.fileName.split('.').pop() || 'FILE';
            return `
            <div class="file-attachment">
                <div class="file-icon-box">
                    <i class="fa-regular fa-file"></i>
                </div>
                <div class="file-info">
                    <span class="file-name">${file.fileName}</span>
                    <span class="file-type">${ext}</span>
                </div>
            </div>`;
        }
    }).join('');

    const usermessageHtml = `
    ${filesHtml ? `<div class="message-files">${filesHtml}</div>` : ''}
    <p class="message-text">${userMessages}</p>
    `;
    const usermessageDiv = createmessageElement(usermessageHtml, "user-message");
    usermessageDiv.querySelector(".message-text").textContent = userMessages;
    chatsContainer.appendChild(usermessageDiv);
    scrollToBottom();
    setTimeout(() => {
        // Create the loading indicator dots container
        const chatbotmessageHtml = `<div class="message-text"><div class="typing-indicator"><span></span><span></span><span></span></div></div>`;
        const chatbotmessageDiv = createmessageElement(chatbotmessageHtml, "chatbot-message", "loading");
        chatsContainer.appendChild(chatbotmessageDiv);
        scrollToBottom();
        generateChatbotResponse(chatbotmessageDiv);
    }, 600);
    promptInput.value = "";
    document.getElementById('file-preview-container').innerHTML = "";

}
const filePreviewContainer = document.getElementById('file-preview-container');

fileInput.addEventListener('change', () => {
    const files = Array.from(fileInput.files);

    // Check if total files will exceed 8
    if (userData.files.length + files.length > 8) {
        alert("You can only upload a maximum of 8 files at a time.");
        fileInput.value = "";
        return;
    }

    files.forEach(file => {
        const isImage = file.type.startsWith("image/");
        const reader = new FileReader();
        reader.readAsDataURL(file);

        reader.onload = (e) => {
            const base64String = e.target.result.split(',')[1];

            // Store file data
            const fileObj = { fileName: file.name, data: base64String, mime_type: file.type, isImage };
            userData.files.push(fileObj);

            // Create preview item DOM
            const previewItem = document.createElement('div');
            previewItem.classList.add('file-preview-item');

            if (isImage) {
                previewItem.innerHTML = `<img src="${e.target.result}" alt="preview">`;
            } else {
                previewItem.innerHTML = `<i class="fa-regular fa-file file-icon"></i>`;
            }

            // Individual cancel button
            const cancelBtn = document.createElement('button');
            cancelBtn.classList.add('cancel-upload-button');
            cancelBtn.type = 'button';
            cancelBtn.innerHTML = '<i class="fa-solid fa-times"></i>';

            cancelBtn.addEventListener('click', () => {
                const index = userData.files.indexOf(fileObj);
                if (index > -1) {
                    userData.files.splice(index, 1);
                }
                previewItem.remove();
            });

            previewItem.appendChild(cancelBtn);
            filePreviewContainer.appendChild(previewItem);
        }
    });

    // Clear input so same file can be uploaded again if removed
    fileInput.value = "";
});
promptForm.addEventListener('submit', handleformSubmit);
document.querySelector('#send-prompt-button').addEventListener('click', handleformSubmit);

document.querySelector('#add-file-button').addEventListener('click', () => {
    fileInput.click();
});

// Profile Data
const fetchUserProfile = async () => {
    try {
        const token = localStorage.getItem('access_token');
        if (!token) return null;

        const res = await fetch(`${API_BASE_URL}/jwt_validation`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (res.ok) {
            const data = await res.json();
            return {
                fullName: data.user.sub || "User",
                role: data.user.role || "Role",
                position: data.user.position || "Position",
                department: data.user.department || "Department"
            };
        } else {
            localStorage.removeItem('access_token');
            window.location.href = '../login page/login.html';
        }
    } catch (e) {
        console.error(e);
    }
    return null;
};

document.addEventListener("DOMContentLoaded", async () => {
    const profileData = await fetchUserProfile();
    if (profileData) {
        document.getElementById("user-fullname").textContent = profileData.fullName;
        document.getElementById("user-role").textContent = profileData.role;
        document.getElementById("user-position").textContent = profileData.position;
        document.getElementById("user-department").textContent = profileData.department;
    }

    const chatHistoryList = document.getElementById("chat-history-list");

    // Hamburger Menu Logic
    const menuBtn = document.getElementById("menu-btn");
    const sidebar = document.querySelector(".sidebar");
    const sidebarOverlay = document.getElementById("sidebar-overlay");

    if (menuBtn && sidebar && sidebarOverlay) {
        menuBtn.addEventListener("click", () => {
            sidebar.classList.toggle("active");
            sidebarOverlay.classList.toggle("active");
        });

        sidebarOverlay.addEventListener("click", () => {
            sidebar.classList.remove("active");
            sidebarOverlay.classList.remove("active");
        });
    }

    // New Chat logic
    const newChatBtn = document.getElementById("new-chat-btn");
    const appHeader = document.querySelector(".app-header");

    const saveCurrentChat = () => {
        const firstUserMessage = document.querySelector(".chats-container .user-message .message-text");
        if (firstUserMessage && chatHistoryList) {
            let previewText = firstUserMessage.textContent.trim();
            if (previewText.length > 25) {
                previewText = previewText.substring(0, 25) + "...";
            }

            // Only add sidebar item if this session wasn't already saved
            if (!savedSessions[currentChatId]) {
                const li = document.createElement("li");
                li.classList.add("chat-history-item");
                li.innerHTML = `<i class="fa-regular fa-message"></i> <span>${previewText}</span>`;
                li.dataset.chatId = currentChatId; // Store ID on the element

                // Add click listener to restore this chat
                li.addEventListener("click", () => {
                    // Save current active chat before swapping
                    if (chatsContainer.children.length > 0) saveCurrentChat();

                    // Restore clicked chat
                    const clickedId = li.dataset.chatId;
                    if (savedSessions[clickedId]) {
                        chatsContainer.innerHTML = savedSessions[clickedId];
                        currentChatId = clickedId;
                        if (appHeader) appHeader.style.display = "none";
                        scrollToBottom();
                    }
                });

                chatHistoryList.insertBefore(li, chatHistoryList.firstChild);
            }
            // Save or update the HTML snapshot in memory
            savedSessions[currentChatId] = chatsContainer.innerHTML;
        }
    };

    if (newChatBtn) {
        newChatBtn.addEventListener("click", () => {
            saveCurrentChat();

            // Wipe the chat container visual and memory for a new session
            if (chatsContainer) chatsContainer.innerHTML = "";
            chatHistory.length = 0;
            currentChatId = Date.now().toString(); // reset ID for new session

            // Reveal Welcome Header
            if (appHeader) appHeader.style.display = ""; // remove inline "none" constraint
        });
    }

    // Logout logic
    const logoutBtn = document.getElementById("logout-btn");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", () => {
            localStorage.removeItem("access_token");
            window.location.href = "../login page/login.html";
        });
    }
});