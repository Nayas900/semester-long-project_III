# quiz_engine.py

import random
from rag_engine import retrieve_context

def generate_quiz(num_questions=5):
    quiz = []

    # Get random concepts
    contexts = retrieve_context("important MCA concepts", top_k=10)
    selected = random.sample(contexts, num_questions)

    for text in selected:
        question = {
            "question": f"What is related to: {text} ?",
            "options": {
                "A": "Correct explanation",
                "B": "Wrong option 1",
                "C": "Wrong option 2",
                "D": "Wrong option 3"
            },
            "correct": "A"
        }
        quiz.append(question)

    return quiz
