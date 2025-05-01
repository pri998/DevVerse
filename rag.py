import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# === Setup Constants ===
MODEL_NAME = 'all-MiniLM-L6-v2'
CHROMA_COLLECTION = "project_docs"
MAX_MATCHES = 5

# === Setup Embedding Model and Chroma Client ===
model = SentenceTransformer(MODEL_NAME)
chroma = chromadb.Client(Settings())
docs = chroma.get_or_create_collection(CHROMA_COLLECTION)

# === Core Logic ===

def generate_embedding(text: str) -> list:
    """Convert text into vector embedding."""
    return model.encode(text).tolist()

def fetch_relevant_data(vector: list) -> tuple:
    """Retrieve top matching documents from ChromaDB."""
    result = docs.query(query_embeddings=[vector], n_results=MAX_MATCHES)
    return result["documents"][0], result["metadatas"][0]

def assemble_context(chunks: list, tags: list) -> str:
    """Format retrieved documents into a readable context block."""
    return "\n\n".join(
        f"🔹 [{tag.get('project')} | {tag.get('type')}] — {text}"
        for text, tag in zip(chunks, tags)
    )

def create_contextual_prompt(query: str, references: str) -> str:
    """Generate the final instruction prompt for the AI agent."""
    return f"""📘 Prompt Context

You are a domain expert.

User Input:
\"\"\"{query}\"\"\"

Reference Snippets:
{references}

Please use the above information to provide a detailed and refined output.
"""

def contextual_generation(user_input: str) -> str:
    """Main RAG function to produce AI-ready prompt."""
    vector = generate_embedding(user_input)
    chunks, tags = fetch_relevant_data(vector)
    context_block = assemble_context(chunks, tags)
    return create_contextual_prompt(user_input, context_block)
