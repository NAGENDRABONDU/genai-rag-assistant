// Generate or get existing session ID
function getSessionId() {
    let sessionId = localStorage.getItem("sessionId");

    if (!sessionId) {
        sessionId = crypto.randomUUID();
        localStorage.setItem("sessionId", sessionId);
    }

    return sessionId;
}

// Add message to chat window
function addMessage(sender, message, className) {
    const chatBox = document.getElementById("chat-box");

    const div = document.createElement("div");
    div.className = `message ${className}`;

    div.innerHTML = `
        <b>${sender}:</b> ${message}
    `;

    chatBox.appendChild(div);

    // Auto-scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message to backend
async function sendMessage() {

    const input = document.getElementById("message");
    const message = input.value.trim();

    if (!message) {
        return;
    }

    // Show user message
    addMessage("You", message, "user");

    // Clear input
    input.value = "";

    // Loading message
    const chatBox = document.getElementById("chat-box");

    const loadingDiv = document.createElement("div");
    loadingDiv.className = "message assistant";
    loadingDiv.id = "loading-message";
    loadingDiv.innerHTML = "<b>Assistant:</b> Thinking...";

    chatBox.appendChild(loadingDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch(
            "https://genai-rag-assistant-production-bd3c.up.railway.app/api/chat",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    sessionId: getSessionId(),
                    message: message
                })
            }
        );

        // Remove loading text
        document
            .getElementById("loading-message")
            ?.remove();

        if (!response.ok) {
            throw new Error(
                `HTTP Error ${response.status}`
            );
        }

        const data = await response.json();

        addMessage(
            "Assistant",
            data.reply,
            "assistant"
        );

    } catch (error) {

        document
            .getElementById("loading-message")
            ?.remove();

        addMessage(
            "Error",
            "Unable to contact backend server.",
            "assistant"
        );

        console.error(error);
    }
}

// Press Enter to send
document.addEventListener(
    "DOMContentLoaded",
    () => {

        const input =
            document.getElementById(
                "message"
            );

        input.addEventListener(
            "keypress",
            function (event) {

                if (
                    event.key === "Enter"
                ) {
                    sendMessage();
                }
            }
        );
    }
);