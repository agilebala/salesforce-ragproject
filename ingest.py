import os
from dotenv import load_dotenv
from pinecone import Pinecone
from utils.chunking import chunk_transcripts
from utils.embedding import get_embedding

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX")
dimension = 1536  # For OpenAI ada-002

# Initialize Pinecone client
pc = Pinecone(api_key=api_key)

# Create the index if it doesn't exist
if index_name not in [idx.name for idx in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine"
    )

index = pc.Index(index_name)

DATA_DIR = "data"

def main():
    docs = chunk_transcripts(DATA_DIR)
    vectors = []
    for i, doc in enumerate(docs):
        embedding = get_embedding(doc['text'])
        vectors.append((
            f"doc-{i}",
            embedding,
            {"text": doc['text'], "source": doc['source']}
        ))
    # Upsert vectors in batches
    batch_size = 100
    for i in range(0, len(vectors), batch_size):
        index.upsert(vectors=vectors[i:i+batch_size])
    print(f"Ingested and indexed {len(docs)} chunks.")

if __name__ == "__main__":
    main()

