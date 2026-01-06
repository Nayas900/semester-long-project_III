# # rag_engine.py
# # Retrieval + Prompt Construction

# import faiss
# import pickle
# from sentence_transformers import SentenceTransformer

# VECTOR_STORE = "vector_store"

# # Load model & data
# model = SentenceTransformer("all-MiniLM-L6-v2")
# index = faiss.read_index(f"{VECTOR_STORE}/faiss.index")

# with open(f"{VECTOR_STORE}/chunks.pkl", "rb") as f:
#     chunks = pickle.load(f)

# def retrieve_context(query, top_k=3):
#     query_vector = model.encode([query])
#     distances, indices = index.search(query_vector, top_k)

#     retrieved_chunks = [chunks[i] for i in indices[0]]
#     return retrieved_chunks

# def generate_answer(query, context):
#     """
#     Replace this with OpenAI / Gemini later
#     """
#     answer = f"Question: {query}\n\nBased on syllabus:\n"
#     for c in context:
#         answer += f"- {c}\n"
#     return answer
# rag_engine.py

import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECTOR_STORE = os.path.join(BASE_DIR, "vector_store")

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(os.path.join(VECTOR_STORE, "faiss.index"))

with open(os.path.join(VECTOR_STORE, "chunks.pkl"), "rb") as f:
    chunks = pickle.load(f)

def retrieve_context(query, top_k=1):
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, top_k)
    return [chunks[i] for i in indices[0]]

def generate_answer(query, context):
    answer = f"Question: {query}\n\nBased on syllabus:\n"
    for c in context:
        answer += f"- {c}\n"
    return answer
