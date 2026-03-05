function setTheme(theme) {
    document.body.className = theme;
}

function updateClock() {
    const now = new Date();
    document.getElementById("utcClock").innerText =
        "UTC Time: " + now.toUTCString();
}
setInterval(updateClock,1000);

async function uploadPDF() {
    const files = document.getElementById("pdfFile").files;
    const formData = new FormData();

    for (let i=0;i<files.length;i++) {
        formData.append("file", files[i]);
    }

    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const result = await response.json();
    document.getElementById("uploadStatus").innerText =
        result.message || result.error;
}

async function sendMessage() {
    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");
    const text = input.value;

    chatBox.innerHTML += `<div class="message user">${text}</div>`;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({query: text})
    });

    const result = await response.json();

    chatBox.innerHTML += `<div class="message bot">${result.answer}</div>`;

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}