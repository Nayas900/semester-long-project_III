from flask import Flask, request, jsonify
from flask_cors import CORS
from rag_engine import retrieve_context, generate_answer
from quiz_engine import generate_quiz

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")

    context = retrieve_context(question)
    answer = generate_answer(question, context)

    return jsonify({
        "question": question,
        "answer": answer
    })

#  QUIZ API
@app.route("/quiz", methods=["GET"])
def quiz():
    quiz_data = generate_quiz()
    return jsonify(quiz_data)

if __name__ == "__main__":
    app.run(debug=True)
