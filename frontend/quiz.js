let quizData = [];

async function loadQuiz() {
    const response = await fetch("http://127.0.0.1:5000/quiz");
    quizData = await response.json();

    const quizDiv = document.getElementById("quiz");
    quizDiv.innerHTML = "";

    quizData.forEach((q, i) => {
        quizDiv.innerHTML += `<p><b>Q${i + 1}. ${q.question}</b></p>`;

        // Randomize options order
        const options = Object.entries(q.options)
            .sort(() => Math.random() - 0.5);

        options.forEach(([key, value]) => {
            quizDiv.innerHTML += `
                <input type="radio" name="q${i}" value="${key}">
                ${key}) ${value}<br>
            `;
        });
    });
}

function submitQuiz() {
    let score = 0;

    quizData.forEach((q, i) => {
        const selected = document.querySelector(`input[name="q${i}"]:checked`);
        if (selected && selected.value === q.correct) {
            score++;
        }
    });

    document.getElementById("result").innerText =
        `Your Score: ${score} / ${quizData.length}`;
}

function goBack() {
    window.location.href = "index.html";
}
