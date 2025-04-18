import os
import uuid
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from typing import List

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("project_docs")

# Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Chunker
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# Load and process .txt files from a project folder
def process_project(project_name: str, folder_path: str):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_type = filename.replace(".txt", "")
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                full_text = f.read()
                chunks = chunk_text(full_text)

                for idx, chunk in enumerate(chunks):
                    embedding = embedder.encode(chunk).tolist()
                    collection.add(
                        documents=[chunk],
                        embeddings=[embedding],
                        metadatas=[{
                            "project": project_name,
                            "type": file_type,
                            "file": filename,
                            "chunk_id": idx
                        }],
                        ids=[str(uuid.uuid4())]
                    )
            print(f"✅ Processed {filename} for {project_name}")

# Example usage
process_project("social_media_clone", "./social_media_clone")
process_project("e_commerce", "./ecommerce")

print("🎉 All documents embedded and stored in ChromaDB!")
print(collection.count())
