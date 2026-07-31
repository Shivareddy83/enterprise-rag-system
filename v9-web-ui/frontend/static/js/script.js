/* ==========================================================
   ENTERPRISE RAG SYSTEM V9
   Frontend JavaScript
   Part 1
========================================================== */

/* ==========================================================
   DOM ELEMENTS
========================================================== */

// Chat
const chatContainer = document.getElementById("chatContainer");

// Input
const questionInput = document.getElementById("questionInput");

// Buttons
const sendButton = document.getElementById("sendButton");
const clearButton = document.getElementById("clearButton");
const themeToggle = document.getElementById("themeToggle");

// Sidebar
const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebarToggle");

// Search
const chatSearch = document.getElementById("chatSearch");

// Export
const exportTxt = document.getElementById("exportTxt");
const exportJson = document.getElementById("exportJson");
const exportPdf = document.getElementById("exportPdf");

// Upload
const uploadButton = document.getElementById("uploadButton");
const pdfFile = document.getElementById("pdfFile");
const uploadStatus = document.getElementById("uploadStatus");

// Chat
const typingIndicator = document.getElementById("typingIndicator");
const toastContainer = document.getElementById("toastContainer");
const statusIndicator = document.getElementById("statusIndicator");

// Example Buttons
const exampleButtons = document.querySelectorAll(".examples button");


/* ==========================================================
   API CONFIGURATION
========================================================== */

const API = {

    BASE_URL: "http://127.0.0.1:8085/api/v1",

    ENDPOINTS: {

        ASK: "/ask",

        UPLOAD: "/upload",

        HEALTH: "/health",

        COUNT: "/debug/count"

    },

    HEADERS: {

        "Content-Type": "application/json"

    }

};


/* ==========================================================
   LOCAL STORAGE
========================================================== */

const STORAGE = {

    CHAT_HISTORY: "enterprise_rag_chat_history",

    THEME: "enterprise_rag_theme",

    SIDEBAR: "enterprise_rag_sidebar"

};


/* ==========================================================
   APPLICATION STATE
========================================================== */

const appState = {

    isLoading: false,

    chatHistory: [],

    currentRequest: null,

    theme: "dark"

};


/* ==========================================================
   INITIALIZATION
========================================================== */

function initializeApplication() {

    registerEvents();

    loadTheme();

    loadSidebar();

    loadChatHistory();

    checkServerHealth();

    questionInput.focus();

    console.clear();

    console.log("====================================");

    console.log("Enterprise RAG System V9");

    console.log("Frontend Started Successfully");

    console.log("====================================");

}


/* ==========================================================
   REGISTER EVENTS
========================================================== */

function registerEvents() {

    // Chat
    sendButton.addEventListener("click", sendMessage);

    clearButton.addEventListener("click", clearChat);

    // Keyboard
    questionInput.addEventListener(

        "keydown",

        handleKeyboard

    );

    // Upload
    if (uploadButton) {

        uploadButton.addEventListener(

            "click",

            uploadPDF

        );

    }

    // Theme
    themeToggle.addEventListener(

        "click",

        toggleTheme

    );

    // Sidebar
    sidebarToggle.addEventListener(

        "click",

        toggleSidebar

    );

    // Search
    chatSearch.addEventListener(

        "input",

        searchMessages

    );

    // Export
    exportTxt.addEventListener(

        "click",

        exportAsText

    );

    exportJson.addEventListener(

        "click",

        exportAsJSON

    );

    exportPdf.addEventListener(

        "click",

        exportAsPDF

    );

    // Examples
    exampleButtons.forEach(button => {

        button.addEventListener(

            "click",

            () => {

                questionInput.value =

                    button.textContent;

                questionInput.focus();

            }

        );

    });

}


/* ==========================================================
   HEALTH CHECK
========================================================== */

async function checkServerHealth() {

    try {

        const response = await fetch(

            API.BASE_URL +

            API.ENDPOINTS.HEALTH

        );

        if (!response.ok) {

            throw new Error();

        }

        statusIndicator.textContent =

            "🟢 Online";

        statusIndicator.style.color =

            "#22c55e";

    }

    catch {

        statusIndicator.textContent =

            "🔴 Offline";

        statusIndicator.style.color =

            "#ef4444";

        showToast(

            "Backend server offline.",

            "warning"

        );

    }

}


/* ==========================================================
   UPLOAD PDF
========================================================== */

async function uploadPDF() {

    const file = pdfFile.files[0];

    if (!file) {

        showToast(

            "Select a PDF first.",

            "warning"

        );

        return;

    }

    const formData = new FormData();

    formData.append(

        "file",

        file

    );

    uploadStatus.textContent =

        "Uploading PDF...";

    try {

        const response = await fetch(

            API.BASE_URL +

            API.ENDPOINTS.UPLOAD,

            {

                method: "POST",

                body: formData

            }

        );

        if (!response.ok) {

            throw new Error();

        }

        const data =

            await response.json();

        uploadStatus.textContent =

            "Upload Successful";

        showToast(

            "PDF Indexed Successfully."

        );

        console.log(data);

    }

    catch (error) {

        uploadStatus.textContent =

            "Upload Failed";

        showToast(

            "Unable to upload PDF.",

            "error"

        );

    }

}


/* ==========================================================
   START APPLICATION
========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    initializeApplication

);
/* ==========================================================
   SEND MESSAGE
========================================================== */

async function sendMessage() {

    if (appState.isLoading) {

        return;

    }

    const question = questionInput.value.trim();

    if (!question) {

        showToast(

            "Please enter a question.",

            "warning"

        );

        questionInput.focus();

        return;

    }

    createUserMessage(question);

    appState.chatHistory.push({

        role: "user",

        content: question

    });

    saveChatHistory();

    questionInput.value = "";

    setLoading(true);

    showTyping();

    try {

        const result = await askQuestion(question);

        hideTyping();

        createAIMessage(result.answer);

        appState.chatHistory.push({

            role: "assistant",

            content: result.answer

        });

        saveChatHistory();

        if (result.context) {

            console.log(

                "Retrieved Context:",

                result.context

            );

        }

    }

    catch (error) {

        hideTyping();

        showError(error.message);

    }

    finally {

        setLoading(false);

        scrollToBottom();

    }

}


/* ==========================================================
   ASK QUESTION API
========================================================== */

async function askQuestion(question) {

    const response = await fetch(

        API.BASE_URL +

        API.ENDPOINTS.ASK,

        {

            method: "POST",

            headers: API.HEADERS,

            body: JSON.stringify({

                question: question

            })

        }

    );

    if (!response.ok) {

        throw new Error(

            "Unable to connect to Enterprise RAG Server."

        );

    }

    return await response.json();

}


/* ==========================================================
   USER MESSAGE
========================================================== */

function createUserMessage(message) {

    const messageElement =

        document.createElement("div");

    messageElement.className =

        "message user-message";

    messageElement.innerHTML = `

        <div class="avatar">

            👤

        </div>

        <div class="text">

            ${escapeHTML(message)}

            <div class="message-footer">

                <span class="message-time">

                    ${formatTime()}

                </span>

            </div>

        </div>

    `;

    chatContainer.appendChild(

        messageElement

    );

    scrollToBottom();

}


/* ==========================================================
   AI MESSAGE
========================================================== */

function createAIMessage(message) {

    const messageElement =

        document.createElement("div");

    messageElement.className =

        "message ai-message";

    messageElement.innerHTML = `

        <div class="avatar">

            🤖

        </div>

        <div class="text">

            ${renderMarkdown(message)}

            <div class="message-footer">

                <span class="message-time">

                    ${formatTime()}

                </span>

                <div class="message-actions">

                    <button
                        class="copy-btn"
                        title="Copy">

                        📋

                    </button>

                    <button
                        class="retry-btn"
                        title="Retry">

                        🔄

                    </button>

                    <button
                        class="delete-btn"
                        title="Delete">

                        🗑

                    </button>

                </div>

            </div>

        </div>

    `;

    chatContainer.appendChild(

        messageElement

    );

    messageElement

        .querySelectorAll("pre code")

        .forEach(block => {

            hljs.highlightElement(block);

        });

    addCopyButtons(messageElement);

    initializeMessageActions(

        messageElement,

        message

    );

    scrollToBottom();

}


/* ==========================================================
   MESSAGE ACTIONS
========================================================== */

function initializeMessageActions(

    messageElement,

    message

) {

    const copyButton =

        messageElement.querySelector(

            ".copy-btn"

        );

    const retryButton =

        messageElement.querySelector(

            ".retry-btn"

        );

    const deleteButton =

        messageElement.querySelector(

            ".delete-btn"

        );

    copyButton.addEventListener(

        "click",

        async () => {

            await navigator.clipboard.writeText(

                message

            );

            showToast(

                "Copied successfully."

            );

        }

    );

    retryButton.addEventListener(

        "click",

        () => {

            const previousQuestion =

                [...appState.chatHistory]

                .reverse()

                .find(

                    msg =>

                    msg.role === "user"

                );

            if (!previousQuestion) {

                showToast(

                    "No previous question.",

                    "warning"

                );

                return;

            }

            questionInput.value =

                previousQuestion.content;

            sendMessage();

        }

    );

    deleteButton.addEventListener(

        "click",

        () => {

            messageElement.remove();

            showToast(

                "Message deleted."

            );

        }

    );

}


/* ==========================================================
   MARKDOWN
========================================================== */

function renderMarkdown(content) {

    return marked.parse(content);

}


/* ==========================================================
   COPY CODE BUTTON
========================================================== */

function addCopyButtons(messageElement) {

    const blocks =

        messageElement.querySelectorAll("pre");

    blocks.forEach(block => {

        const button =

            document.createElement("button");

        button.className =

            "copy-code-btn";

        button.textContent =

            "📋 Copy";

        button.addEventListener(

            "click",

            async () => {

                const code =

                    block.querySelector("code")

                    .innerText;

                await navigator.clipboard.writeText(

                    code

                );

                showToast(

                    "Code copied."

                );

            }

        );

        block.appendChild(button);

    });

}


/* ==========================================================
   TYPING INDICATOR
========================================================== */

function showTyping() {

    typingIndicator.classList.add(

        "active"

    );

    scrollToBottom();

}

function hideTyping() {

    typingIndicator.classList.remove(

        "active"

    );

}
/* ==========================================================
   AUTO SCROLL
========================================================== */

function scrollToBottom() {

    chatContainer.scrollTo({

        top: chatContainer.scrollHeight,

        behavior: "smooth"

    });

}


/* ==========================================================
   LOADING STATE
========================================================== */

function setLoading(status) {

    appState.isLoading = status;

    sendButton.disabled = status;

    questionInput.disabled = status;

    if (uploadButton) {

        uploadButton.disabled = status;

    }

    sendButton.textContent =

        status

            ? "Sending..."

            : "Send";

}


/* ==========================================================
   TOAST NOTIFICATION
========================================================== */

function showToast(

    message,

    type = "success"

) {

    const toast =

        document.createElement("div");

    toast.className =

        `toast ${type}`;

    toast.textContent =

        message;

    toastContainer.appendChild(

        toast

    );

    requestAnimationFrame(() => {

        toast.classList.add(

            "show"

        );

    });

    setTimeout(() => {

        toast.classList.remove(

            "show"

        );

        setTimeout(() => {

            toast.remove();

        }, 300);

    }, 2500);

}


/* ==========================================================
   ERROR HANDLING
========================================================== */

function showError(message) {

    createAIMessage(

        `❌ **Error**\n\n${message}`

    );

    showToast(

        message,

        "error"

    );

}


/* ==========================================================
   TIME
========================================================== */

function formatTime() {

    return new Date()

        .toLocaleTimeString(

            [],

            {

                hour: "2-digit",

                minute: "2-digit"

            }

        );

}


/* ==========================================================
   ESCAPE HTML
========================================================== */

function escapeHTML(text) {

    const div =

        document.createElement("div");

    div.textContent =

        text;

    return div.innerHTML;

}


/* ==========================================================
   DOWNLOAD FILE
========================================================== */

function downloadFile(

    content,

    filename,

    type

) {

    const blob =

        new Blob(

            [content],

            {

                type

            }

        );

    const url =

        URL.createObjectURL(blob);

    const link =

        document.createElement("a");

    link.href = url;

    link.download = filename;

    document.body.appendChild(link);

    link.click();

    link.remove();

    URL.revokeObjectURL(url);

}


/* ==========================================================
   THEME
========================================================== */

function toggleTheme() {

    document.body.classList.toggle(

        "light-theme"

    );

    const isLight =

        document.body.classList.contains(

            "light-theme"

        );

    themeToggle.textContent =

        isLight

            ? "☀️"

            : "🌙";

    localStorage.setItem(

        STORAGE.THEME,

        isLight

            ? "light"

            : "dark"

    );

}


function loadTheme() {

    const theme =

        localStorage.getItem(

            STORAGE.THEME

        );

    if (theme === "light") {

        document.body.classList.add(

            "light-theme"

        );

        themeToggle.textContent =

            "☀️";

    }

    else {

        themeToggle.textContent =

            "🌙";

    }

}


/* ==========================================================
   SIDEBAR
========================================================== */

function toggleSidebar() {

    sidebar.classList.toggle(

        "collapsed"

    );

    localStorage.setItem(

        STORAGE.SIDEBAR,

        sidebar.classList.contains(

            "collapsed"

        )

    );

}


function loadSidebar() {

    const collapsed =

        localStorage.getItem(

            STORAGE.SIDEBAR

        );

    if (collapsed === "true") {

        sidebar.classList.add(

            "collapsed"

        );

    }

}


/* ==========================================================
   SEARCH CHAT
========================================================== */

function searchMessages(event) {

    const query =

        event.target.value

        .toLowerCase()

        .trim();

    const messages =

        document.querySelectorAll(

            ".message"

        );

    messages.forEach(message => {

        if (!query) {

            message.style.display =

                "flex";

            return;

        }

        const text =

            message.innerText

            .toLowerCase();

        message.style.display =

            text.includes(query)

                ? "flex"

                : "none";

    });

}


/* ==========================================================
   LOCAL STORAGE
========================================================== */

function saveChatHistory() {

    localStorage.setItem(

        STORAGE.CHAT_HISTORY,

        JSON.stringify(

            appState.chatHistory

        )

    );

}


function loadChatHistory() {

    const saved =

        localStorage.getItem(

            STORAGE.CHAT_HISTORY

        );

    if (!saved) {

        return;

    }

    appState.chatHistory =

        JSON.parse(saved);

    chatContainer.innerHTML = "";

    appState.chatHistory.forEach(

        message => {

            if (

                message.role ===

                "user"

            ) {

                createUserMessage(

                    message.content

                );

            }

            else {

                createAIMessage(

                    message.content

                );

            }

        }

    );

}
/* ==========================================================
   EXPORT CHAT
========================================================== */

function exportAsText() {

    let content = "";

    appState.chatHistory.forEach(message => {

        content +=

`${message.role.toUpperCase()}

${message.content}

`;

    });

    downloadFile(

        content,

        "Enterprise_RAG_Chat.txt",

        "text/plain"

    );

    showToast(

        "TXT exported successfully."

    );

}


/* ==========================================================
   EXPORT JSON
========================================================== */

function exportAsJSON() {

    downloadFile(

        JSON.stringify(

            appState.chatHistory,

            null,

            4

        ),

        "Enterprise_RAG_Chat.json",

        "application/json"

    );

    showToast(

        "JSON exported successfully."

    );

}


/* ==========================================================
   EXPORT PDF
========================================================== */

async function exportAsPDF() {

    const { jsPDF } = window.jspdf;

    const pdf = new jsPDF();

    let y = 20;

    pdf.setFontSize(18);

    pdf.text(

        "Enterprise RAG Chat",

        20,

        y

    );

    y += 15;

    pdf.setFontSize(11);

    appState.chatHistory.forEach(message => {

        pdf.text(

            message.role.toUpperCase(),

            20,

            y

        );

        y += 7;

        const lines = pdf.splitTextToSize(

            message.content,

            170

        );

        pdf.text(

            lines,

            20,

            y

        );

        y += lines.length * 7 + 8;

        if (y > 270) {

            pdf.addPage();

            y = 20;

        }

    });

    pdf.save("Enterprise_RAG_Chat.pdf");

    showToast(

        "PDF exported successfully."

    );

}


/* ==========================================================
   DEBUG COUNT
========================================================== */

async function loadStatistics() {

    try {

        const response = await fetch(

            API.BASE_URL +

            API.ENDPOINTS.COUNT

        );

        if (!response.ok) {

            return;

        }

        const data = await response.json();

        console.log(

            "Statistics:",

            data

        );

    }

    catch (error) {

        console.warn(

            "Statistics unavailable."

        );

    }

}


/* ==========================================================
   KEYBOARD SHORTCUTS
========================================================== */

function handleKeyboard(event) {

    if (

        event.key === "Enter"

        &&

        !event.shiftKey

    ) {

        event.preventDefault();

        sendMessage();

    }

}


/* ==========================================================
   CLEAR CHAT
========================================================== */

function clearChat() {

    if (

        !confirm(

            "Clear the complete chat history?"

        )

    ) {

        return;

    }

    appState.chatHistory = [];

    localStorage.removeItem(

        STORAGE.CHAT_HISTORY

    );

    chatContainer.innerHTML = `

    <div class="message ai-message">

        <div class="avatar">

            🤖

        </div>

        <div class="text">

            Welcome 👋

            <br><br>

            Enterprise RAG Assistant is ready.

            Upload your PDF and ask questions.

        </div>

    </div>

    `;

    showToast(

        "Chat cleared."

    );

}


/* ==========================================================
   DRAG & DROP SUPPORT
========================================================== */

if (pdfFile) {

    document.addEventListener(

        "dragover",

        event => {

            event.preventDefault();

        }

    );

    document.addEventListener(

        "drop",

        event => {

            event.preventDefault();

        }

    );

}


/* ==========================================================
   APPLICATION STARTUP
========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        initializeApplication();

        checkServerHealth();

        loadStatistics();

    }

);