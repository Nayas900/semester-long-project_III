async function askQuestion() {
    const questionInput = document.getElementById("question");
    const question = questionInput.value.trim();

    if (question === "") return;

    const chatContainer = document.getElementById("chat-container");

    // 1️⃣ Show user message
    const userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.innerText = question;
    chatContainer.appendChild(userMsg);

    chatContainer.scrollTop = chatContainer.scrollHeight;
    questionInput.value = "";

    // 2️⃣ Fetch answer from backend
    const response = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
    });

    const data = await response.json();

    // 3️⃣ Show bot message
    const botMsg = document.createElement("div");
    botMsg.className = "message bot";
    botMsg.innerText = data.answer;
    chatContainer.appendChild(botMsg);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function goToQuiz() {
    window.location.href = "quiz.html";
}
