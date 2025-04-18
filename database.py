# # # # import os
# # # # import uuid
# # # # import chromadb
# # # # from chromadb.config import Settings
# # # # from sentence_transformers import SentenceTransformer
# # # # from typing import List

# # # # # Initialize ChromaDB
# # # # client = chromadb.Client(Settings())
# # # # collection = client.get_or_create_collection("project_docs")

# # # # # Load embedding model
# # # # embedder = SentenceTransformer('all-MiniLM-L6-v2')

# # # # # Chunker
# # # # def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
# # # #     chunks = []
# # # #     start = 0
# # # #     while start < len(text):
# # # #         end = min(start + chunk_size, len(text))
# # # #         chunks.append(text[start:end])
# # # #         start += chunk_size - overlap
# # # #     return chunks

# # # # # Load and process .txt files from a project folder
# # # # def process_project(project_name: str, folder_path: str):
# # # #     for filename in os.listdir(folder_path):
# # # #         if filename.endswith('.txt'):
# # # #             file_type = filename.replace(".txt", "")
# # # #             with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
# # # #                 full_text = f.read()
# # # #                 chunks = chunk_text(full_text)

# # # #                 for idx, chunk in enumerate(chunks):
# # # #                     embedding = embedder.encode(chunk).tolist()
# # # #                     collection.add(
# # # #                         documents=[chunk],
# # # #                         embeddings=[embedding],
# # # #                         metadatas=[{
# # # #                             "project": project_name,
# # # #                             "type": file_type,
# # # #                             "file": filename,
# # # #                             "chunk_id": idx
# # # #                         }],
# # # #                         ids=[str(uuid.uuid4())]
# # # #                     )
# # # #             print(f"✅ Processed {filename} for {project_name}")

# # # # # Example usage
# # # # process_project("social_media_clone", "./social_media_clone")
# # # # process_project("e_commerce", "./ecommerce")

# # # # print("🎉 All documents embedded and stored in ChromaDB!")

# # # # TOP_K = 5

# # # # # === RAG Function ===
# # # # def retrieve_and_generate(input_text: str):
# # # #     # 1. Embed the input text
# # # #     input_embedding = embedder.encode(input_text).tolist()

# # # #     # 2. Query ChromaDB for similar chunks
# # # #     results = collection.query(
# # # #         query_embeddings=[input_embedding],
# # # #         n_results=TOP_K
# # # #     )

# # # #     # 3. Extract relevant chunks and metadata
# # # #     retrieved_chunks = results['documents'][0]
# # # #     metadatas = results['metadatas'][0]

# # # #     # 4. Build final prompt for LLM
# # # #     context = ""
# # # #     for idx, chunk in enumerate(retrieved_chunks):
# # # #         meta = metadatas[idx]
# # # #         context += f"[{meta['project']} - {meta['type']}] → {chunk}\n\n"

# # # #     final_prompt = f"""
# # # #     You are an expert business analyst.

# # # #     Given the following requirement:

# # # #     \"\"\"{input_text}\"\"\"

# # # #     Here are some relevant business requirements from past projects:

# # # #     {context}

# # # #     Use the above as reference and provide refined output accordingly.
# # # #     """

# # # #     print("🧠 Final Prompt for LLM:")
# # # #     print("=" * 60)
# # # #     print(final_prompt)
# # # #     return final_prompt

# # # # # === Example Call ===
# # # # input_string = "The system should allow users to add groceries to a cart and check out securely."
# # # # prompt = retrieve_and_generate(input_string)


# # # import os
# # # import uuid
# # # import chromadb
# # # from chromadb.config import Settings
# # # from sentence_transformers import SentenceTransformer
# # # from typing import List

# # # # Initialize ChromaDB
# # # client = chromadb.PersistentClient(path="./chroma_db")
# # # collection = client.get_or_create_collection("project_docs")

# # # # Load embedding model
# # # embedder = SentenceTransformer('all-MiniLM-L6-v2')

# # # # Chunker
# # # def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
# # #     chunks = []
# # #     start = 0
# # #     while start < len(text):
# # #         end = min(start + chunk_size, len(text))
# # #         chunks.append(text[start:end])
# # #         start += chunk_size - overlap
# # #     return chunks

# # # # # Load and process .txt files from a project folder
# # # def process_project(project_name: str, folder_path: str):
# # # #     for filename in os.listdir(folder_path):
# # # #         if filename.endswith('.txt'):
# # # #             file_type = filename.replace(".txt", "")
# # # #             with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
# # # #                 full_text = f.read()
# # # #                 chunks = chunk_text(full_text)

# # # #                 for idx, chunk in enumerate(chunks):
# # # #                     embedding = embedder.encode(chunk).tolist()
# # # #                     collection.add(
# # # #                         documents=[chunk],
# # # #                         embeddings=[embedding],
# # # #                         metadatas=[{
# # # #                             "project": project_name,
# # # #                             "type": file_type,
# # # #                             "file": filename,
# # # #                             "chunk_id": idx
# # # #                         }],
# # # #                         ids=[str(uuid.uuid4())]
# # # #                     )
# # # #             print(f"✅ Processed {filename} for {project_name}")

# # #     for idx, chunk in enumerate(chunks):
# # #         embedding = embedder.encode(chunk).tolist()
# # #         print(f"Generated embedding for chunk {idx} of {filename}: {embedding[:5]}...")  # Print first 5 elements for debugging
# # #         collection.add(
# # #             documents=[chunk],
# # #             embeddings=[embedding],
# # #             metadatas=[{
# # #                 "project": project_name,
# # #                 "type": file_type,
# # #                 "file": filename,
# # #                 "chunk_id": idx
# # #             }],
# # #             ids=[str(uuid.uuid4())]
# # #         )


# # # # Example usage
# # # process_project("social_media_clone", "./social_media_clone")
# # # process_project("e_commerce", "./ecommerce")

# # # print("🎉 All documents embedded and stored in ChromaDB!")
# # # print(collection.count())



# # import os
# # import uuid
# # import chromadb
# # from chromadb.config import Settings
# # from sentence_transformers import SentenceTransformer
# # from typing import List

# # # Initialize ChromaDB
# # client = chromadb.PersistentClient(path="./chroma_db")
# # collection = client.get_or_create_collection("project_docs")

# # # Load embedding model
# # embedder = SentenceTransformer('all-MiniLM-L6-v2')

# # # Chunker function to divide text into smaller chunks
# # def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
# #     chunks = []
# #     start = 0
# #     while start < len(text):
# #         end = min(start + chunk_size, len(text))
# #         chunks.append(text[start:end])
# #         start += chunk_size - overlap
# #     return chunks

# # # Load and process .txt files from a project folder
# # def process_project(project_name: str, folder_path: str):
# #     for filename in os.listdir(folder_path):
# #         if filename.endswith('.txt'):  # Only process .txt files
# #             file_type = filename.replace(".txt", "")
# #             with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
# #                 full_text = f.read()  # Read the file content
# #                 chunks = chunk_text(full_text)  # Split the content into chunks

# #                 # Loop through each chunk and process it
# #                 for idx, chunk in enumerate(chunks):
# #                     embedding = embedder.encode(chunk).tolist()  # Generate embedding for each chunk
# #                     print(f"Generated embedding for chunk {idx} of {filename}: {embedding[:5]}...")  # Print first 5 elements for debugging
                    
# #                     # Add document, embedding, and metadata to ChromaDB collection
# #                     collection.add(
# #                         documents=[chunk],
# #                         embeddings=[embedding],
# #                         metadatas=[{
# #                             "project": project_name,
# #                             "type": file_type,
# #                             "file": filename,
# #                             "chunk_id": idx
# #                         }],
# #                         ids=[str(uuid.uuid4())]  # Unique ID for each chunk
# #                     )
# #             print(f"✅ Processed {filename} for {project_name}")

# # # Example usage to process projects
# # process_project("social_media_clone", "./social_media_clone")
# # process_project("e_commerce", "./ecommerce")

# # print("🎉 All documents embedded and stored in ChromaDB!")

# # # Check the count of documents in the collection
# # print(f"Total documents in the collection: {collection.count()}")



# # import os
# # from sentence_transformers import SentenceTransformer
# # import chromadb
# # from chromadb.config import Settings
# # from tqdm import tqdm
# # import json

# # # Initialize the sentence transformer model for embedding generation
# # embedder = SentenceTransformer('all-MiniLM-L6-v2')

# # # Set up ChromaDB client and database
# # client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="db"))
# # collection = client.get_or_create_collection("documents_collection")

# # # Function to load and process text files
# # def load_text_files(directory):
# #     files_data = {}
# #     for filename in os.listdir(directory):
# #         if filename.endswith(".txt"):
# #             file_path = os.path.join(directory, filename)
# #             with open(file_path, 'r') as file:
# #                 content = file.read()
# #                 files_data[filename] = content
# #     return files_data

# # # Function to split the content into chunks for embedding
# # def split_into_chunks(text, chunk_size=500):
# #     chunks = []
# #     start = 0
# #     while start < len(text):
# #         end = start + chunk_size
# #         chunks.append(text[start:end])
# #         start = end
# #     return chunks

# # # Function to embed and store chunks in ChromaDB
# # def embed_and_store_data(directory):
# #     # Load text files
# #     files_data = load_text_files(directory)
    
# #     # Iterate through each file and process its content
# #     for file_name, content in files_data.items():
# #         chunks = split_into_chunks(content)
# #         embeddings = []

# #         for i, chunk in enumerate(tqdm(chunks, desc=f"Processing {file_name}")):
# #             # Create embedding for each chunk
# #             embedding = embedder.encode(chunk).tolist()
# #             embeddings.append(embedding)

# #             # Store each chunk with metadata (e.g., file name, chunk index)
# #             collection.add(
# #                 documents=[chunk],
# #                 embeddings=[embedding],
# #                 metadatas=[{"file_name": file_name, "chunk_index": i}],
# #                 ids=[f"{file_name}_{i}"]
# #             )
# #             print(f"Generated embedding for chunk {i} of {file_name}: {embedding[:5]}...")

# #         print(f"✅ Processed {file_name}")

# # # Function to query the collection for relevant documents
# # def retrieve_and_generate(input_text: str, top_k=5):
# #     # 1. Embed the input query
# #     input_embedding = embedder.encode(input_text).tolist()

# #     # 2. Query ChromaDB for the most similar chunks
# #     results = collection.query(
# #         query_embeddings=[input_embedding],
# #         n_results=top_k
# #     )

# #     # 3. Extract the relevant documents and metadata
# #     retrieved_chunks = results['documents'][0]
# #     metadatas = results['metadatas'][0]

# #     # 4. Build a prompt for a language model with context
# #     context = ""
# #     for idx, chunk in enumerate(retrieved_chunks):
# #         meta = metadatas[idx]
# #         context += f"[{meta['file_name']} - Chunk {meta['chunk_index']}] → {chunk}\n\n"

# #     final_prompt = f"""
# #     You are an expert business analyst.

# #     Given the following requirement:

# #     \"\"\"{input_text}\"\"\"

# #     Here are some relevant business requirements from past projects:

# #     {context}

# #     Use the above as reference and provide refined output accordingly.
# #     """

# #     print("🧠 Final Prompt for LLM:")
# #     print("=" * 60)
# #     print(final_prompt)
# #     return final_prompt

# # # Main function to initialize database and embed documents
# # def main():
# #     directory = "your_text_files_directory"  # Directory containing your text files
# #     print("📚 Embedding and storing documents...")
# #     embed_and_store_data(directory)
# #     print("🎉 All documents embedded and stored in ChromaDB!")

# # # If running this script directly, execute the main function
# # if __name__ == "__main__":
# #     main()


# import os
# from sentence_transformers import SentenceTransformer
# import chromadb
# from chromadb.config import Settings
# from tqdm import tqdm
# import json

# # Initialize the sentence transformer model for embedding generation
# embedder = SentenceTransformer('all-MiniLM-L6-v2')

# # Set up ChromaDB client and database
# persist_dir = "db"  # Ensure this directory exists
# client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=persist_dir))
# collection = client.get_or_create_collection("documents_collection")

# # Function to load and process text files
# def load_text_files(directory):
#     if not os.path.exists(directory):
#         print(f"❌ Directory '{directory}' not found!")
#         return {}
    
#     files_data = {}
#     for filename in os.listdir(directory):
#         if filename.endswith(".txt"):
#             file_path = os.path.join(directory, filename)
#             with open(file_path, 'r') as file:
#                 content = file.read()
#                 files_data[filename] = content
#     return files_data

# # Function to split the content into chunks for embedding
# def split_into_chunks(text, chunk_size=500):
#     chunks = []
#     start = 0
#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start = end
#     return chunks

# # Function to embed and store chunks in ChromaDB
# def embed_and_store_data(directory):
#     # Load text files
#     files_data = load_text_files(directory)
    
#     if not files_data:
#         return  # Exit if no files are found
    
#     # Iterate through each file and process its content
#     for file_name, content in files_data.items():
#         chunks = split_into_chunks(content)
#         embeddings = []

#         for i, chunk in enumerate(tqdm(chunks, desc=f"Processing {file_name}")):
#             # Create embedding for each chunk
#             embedding = embedder.encode(chunk).tolist()
#             embeddings.append(embedding)

#             # Store each chunk with metadata (e.g., file name, chunk index)
#             collection.add(
#                 documents=[chunk],
#                 embeddings=[embedding],
#                 metadatas=[{"file_name": file_name, "chunk_index": i}],
#                 ids=[f"{file_name}_{i}"]
#             )
#             print(f"Generated embedding for chunk {i} of {file_name}: {embedding[:5]}...")

#         print(f"✅ Processed {file_name}")

# # Function to query the collection for relevant documents
# def retrieve_and_generate(input_text: str, top_k=5):
#     # 1. Embed the input query
#     input_embedding = embedder.encode(input_text).tolist()

#     # 2. Query ChromaDB for the most similar chunks
#     results = collection.query(
#         query_embeddings=[input_embedding],
#         n_results=top_k
#     )

#     # 3. Extract the relevant documents and metadata
#     retrieved_chunks = results['documents'][0]
#     metadatas = results['metadatas'][0]

#     # 4. Build a prompt for a language model with context
#     context = ""
#     for idx, chunk in enumerate(retrieved_chunks):
#         meta = metadatas[idx]
#         context += f"[{meta['file_name']} - Chunk {meta['chunk_index']}] → {chunk}\n\n"

#     final_prompt = f"""
#     You are an expert business analyst.

#     Given the following requirement:

#     \"\"\"{input_text}\"\"\" 

#     Here are some relevant business requirements from past projects:

#     {context}

#     Use the above as reference and provide refined output accordingly.
#     """

#     print("🧠 Final Prompt for LLM:")
#     print("=" * 60)
#     print(final_prompt)
#     return final_prompt

# # Main function to initialize database and embed documents
# def main():
#     directory = "your_text_files_directory"  # Directory containing your text files
#     if not os.path.exists(directory):
#         print(f"❌ Directory '{directory}' does not exist!")
#         return
#     print("📚 Embedding and storing documents...")
#     embed_and_store_data(directory)
#     print("🎉 All documents embedded and stored in ChromaDB!")

# # If running this script directly, execute the main function
# if __name__ == "__main__":
#     main()

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
