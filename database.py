import os
import uuid
from typing import List
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# === ChromaDB Client Setup ===
db = chromadb.PersistentClient(path="./chroma_db")
repo = db.get_or_create_collection("project_docs")

# === Embedding Model ===
vectorizer = SentenceTransformer("all-MiniLM-L6-v2")

# === Text Chunking Utility ===
def split_into_chunks(data: str, size: int = 500, step: int = 450) -> List[str]:
    segments = []
    for i in range(0, len(data), step):
        piece = data[i:i + size]
        segments.append(piece)
    return segments

# === File Ingestion & Embedding Pipeline ===
def ingest_directory(project_id: str, directory_path: str):
    for file in os.listdir(directory_path):
        if file.endswith(".txt"):
            category = file.replace(".txt", "")
            full_path = os.path.join(directory_path, file)

            with open(full_path, 'r', encoding='utf-8') as handle:
                content = handle.read()
                blocks = split_into_chunks(content)

                for index, block in enumerate(blocks):
                    vec = vectorizer.encode(block).tolist()
                    doc_id = str(uuid.uuid4())

                    repo.add(
                        documents=[block],
                        embeddings=[vec],
                        metadatas=[{
                            "project": project_id,
                            "section": category,
                            "filename": file,
                            "block_index": index
                        }],
                        ids=[doc_id]
                    )
            print(f"📄 {file} from '{project_id}' indexed.")

# === Run Indexing ===
ingest_directory("social_media_platform", "./social_media_clone")
ingest_directory("shop_system", "./ecommerce")

print("✅ Indexing complete.")
print(f"📊 Total documents in DB: {repo.count()}")
