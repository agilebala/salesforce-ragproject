import os
from dotenv import load_dotenv
from pinecone import Pinecone
from utils.embedding import get_embedding

# Load environment variables
load_dotenv()

# Get Pinecone settings from .env
api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX")

# Initialize Pinecone client
pc = Pinecone(api_key=api_key)
index = pc.Index(index_name)

def retrieve_top_k(query, k=5):
    # Get embedding for the query
    query_embedding = get_embedding(query)
    # Query Pinecone index for top-k matches
    results = index.query(
        vector=query_embedding,
        top_k=k,
        include_metadata=True
    )
    context_chunks = []
    for match in results['matches']:
        chunk = {
            'text': match['metadata']['text'],
            'source': match['metadata']['source']
        }
        context_chunks.append(chunk)
    return context_chunks

