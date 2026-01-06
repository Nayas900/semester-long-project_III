import json
from openai import OpenAI

client = OpenAI()


def generate_quiz(num_questions=4):

    prompt = f"""
You are an academic quiz generator for MCA students.

Generate EXACTLY {num_questions} random multiple-choice questions
ONLY from the following subjects:
- Computer Networks (CN)
- Operating Systems (OS)
- Database Management Systems (DBMS)
- Data Structures and Algorithms (DSA)

Rules:
- Questions must be short and exam-oriented
- Each question must have exactly 4 options (A, B, C, D)
- Only ONE correct answer
- Questions should be RANDOM each time
- Do NOT include programming syntax questions
- Do NOT include any other subjects
- Output ONLY valid JSON (no explanations)

JSON format:
[
  {{
    "question": "",
    "options": {{
      "A": "",
      "B": "",
      "C": "",
      "D": ""
    }},
    "correct": ""
  }}
]
"""

    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt
    )

    quiz_text = response.output_text.strip()
    quiz = json.loads(quiz_text)

    return quiz
