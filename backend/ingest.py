# import os
# import faiss
# import pickle
# from sentence_transformers import SentenceTransformer

# # --- PATH SETUP ---
# # This finds the folder where ingest.py is located (the 'backend' folder)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Construct paths relative to the script location
# DATA_PATH = os.path.join(BASE_DIR, "data", "mca_notes.txt")
# VECTOR_STORE = os.path.join(BASE_DIR, "vector_store")

# # Ensure the vector_store folder exists inside the backend folder
# os.makedirs(VECTOR_STORE, exist_ok=True)

# # --- STEP 1: Load Embedding Model ---
# print("Loading model...")
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # --- STEP 2: Read Data ---
# if not os.path.exists(DATA_PATH):
#     print(f"Error: Could not find the file at {DATA_PATH}")
#     exit()

# with open(DATA_PATH, "r", encoding="utf-8") as f:
#     text = f.read()

# # --- STEP 3: Chunking ---
# # Simple line-based chunking
# chunks = [line.strip() for line in text.split("\n") if line.strip()]

# # --- STEP 4: Generate Embeddings ---
# print(f"Generating embeddings for {len(chunks)} chunks...")
# embeddings = model.encode(chunks)

# # --- STEP 5: Create and Save FAISS Index ---
# dimension = embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(embeddings)

# # Save index and chunks to the vector_store folder
# faiss.write_index(index, os.path.join(VECTOR_STORE, "faiss.index"))
# with open(os.path.join(VECTOR_STORE, "chunks.pkl"), "wb") as f:
#     pickle.dump(chunks, f)

# print("Success! Knowledge Brain Built Successfully!")
import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
VECTOR_STORE = os.path.join(BASE_DIR, "vector_store")

os.makedirs(VECTOR_STORE, exist_ok=True)

# Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Chunking function
def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

# Load all txt files
all_chunks = []

for file in os.listdir(DATA_DIR):
    if file.endswith(".txt"):
        file_path = os.path.join(DATA_DIR, file)
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        chunks = chunk_text(text)
        for c in chunks:
            all_chunks.append(f"[{file}] {c}")

print(f"Total chunks created: {len(all_chunks)}")

# Create embeddings
embeddings = model.encode(all_chunks, show_progress_bar=True)

# FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and chunks
faiss.write_index(index, os.path.join(VECTOR_STORE, "faiss.index"))

with open(os.path.join(VECTOR_STORE, "chunks.pkl"), "wb") as f:
    pickle.dump(all_chunks, f)

print(" Vector store updated successfully")
