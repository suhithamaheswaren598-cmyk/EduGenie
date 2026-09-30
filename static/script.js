async function sendRequest(endpoint, text) {
    const response = await fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || "Something went wrong.");
    }

    return data;
}


// ==================== Q&A ====================

async function askQuestion() {
    const question = document.getElementById("question").value;
    const result = document.getElementById("qaResult");

    if (!question.trim()) {
        result.textContent = "Please enter a question.";
        return;
    }

    result.textContent = "EduGenie is thinking...";

    try {
        const data = await sendRequest("/qa", question);
        result.textContent = data.result;
    } catch (error) {
        result.textContent = "Error: " + error.message;
    }
}


// ==================== EXPLANATION ====================

async function explainTopic() {
    const topic = document.getElementById("topic").value;
    const result = document.getElementById("explainResult");

    if (!topic.trim()) {
        result.textContent = "Please enter a topic.";
        return;
    }

    result.textContent = "EduGenie is preparing the explanation...";

    try {
        const data = await sendRequest("/explain", topic);
        result.textContent = data.result;
    } catch (error) {
        result.textContent = "Error: " + error.message;
    }
}


// ==================== QUIZ ====================

async function generateQuiz() {
    const content = document.getElementById("quizContent").value;
    const result = document.getElementById("quizResult");

    if (!content.trim()) {
        result.textContent = "Please enter some content.";
        return;
    }

    result.textContent = "Generating quiz...";

    try {
        const data = await sendRequest("/quiz", content);

        result.innerHTML = "";

        data.result.forEach((item, index) => {

            const questionDiv = document.createElement("div");
            questionDiv.className = "quiz-question";

            const title = document.createElement("h3");
            title.textContent = "Question " + (index + 1);

            const question = document.createElement("p");
            question.textContent = item.question;

            questionDiv.appendChild(title);
            questionDiv.appendChild(question);

            item.options.forEach(option => {

                const button = document.createElement("button");

                button.textContent = option;
                button.className = "quiz-option";

                button.onclick = function () {

                    const feedback =
                        questionDiv.querySelector(".quiz-feedback");

                    if (option === item.correct_answer) {

                        feedback.textContent =
                            "Correct! " + item.explanation;

                    } else {

                        feedback.textContent =
                            "Incorrect. Correct answer: " +
                            item.correct_answer +
                            ". " +
                            item.explanation;
                    }
                };

                questionDiv.appendChild(button);
            });

            const feedback = document.createElement("p");

            feedback.className = "quiz-feedback";
            feedback.style.fontWeight = "bold";

            questionDiv.appendChild(feedback);

            const separator = document.createElement("hr");

            questionDiv.appendChild(separator);

            result.appendChild(questionDiv);
        });

    } catch (error) {

        result.textContent = "Error: " + error.message;
    }
}


// ==================== SUMMARY ====================

async function summarizeText() {
    const text = document.getElementById("summaryText").value;
    const result = document.getElementById("summaryResult");

    if (!text.trim()) {
        result.textContent = "Please enter some text.";
        return;
    }

    result.textContent = "Summarizing...";

    try {
        const data = await sendRequest("/summarize", text);
        result.textContent = data.result;
    } catch (error) {
        result.textContent = "Error: " + error.message;
    }
}


// ==================== LEARNING PATH ====================

async function getLearningPath() {
    const topic = document.getElementById("learningTopic").value;
    const result = document.getElementById("learningResult");

    if (!topic.trim()) {
        result.textContent = "Please enter a topic.";
        return;
    }

    result.textContent = "Creating your learning path...";

    try {
        const data = await sendRequest(
            "/learn/recommendations",
            topic
        );

        result.textContent = data.result;

    } catch (error) {

        result.textContent = "Error: " + error.message;
    }
}


// ==================== TASK DROPDOWN ====================

function showSelectedTask() {

    const task = document.getElementById("taskSelector").value;
    const message = document.getElementById("taskMessage");

    const taskNames = {

        qa: "Ask EduGenie your academic question.",

        explain: "Enter a topic to get a simple explanation.",

        quiz: "Enter educational content to generate 3 MCQs.",

        summary: "Paste educational content to create a summary.",

        learning: "Enter a topic to create a personalized learning path."
    };

    if (task === "") {

        message.textContent =
            "Select a task to get started.";

    } else {

        message.textContent =
            taskNames[task];
    }
}