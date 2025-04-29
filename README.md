Salesforce Earnings Call RAG Project 

A scalable Retrieval-Augmented Generation (RAG) system for Q&A and summarization of Salesforce’s quarterly earnings transcripts, powered by OpenAI and Pinecone, with a simple Streamlit UI.
Features
Conversational Q&A and summarization over Salesforce earnings transcripts
Retrieval-Augmented Generation: Combines LLM output with contextually relevant transcript chunks
Semantic search using Pinecone vector database
Streamlit UI for interactive analyst experience
Handles both structured and unstructured data
Folder structure as below 
salesforce-rag/
├── app.py
├── ingest.py
├── requirements.txt
├── .env
├── README.md
├── data/                # Place your .txt transcripts here
└── utils/
    ├── __init__.py
    ├── chunking.py
    ├── embedding.py
    └── retrieval.py
Prerequisites
Python 3.8+
OpenAI account & API key
Pinecone account & API key
(Optional) GitHub account for version control
Setup instructions 

1. Clone the Repository
   https://github.com/agilebala/salesforce-ragproject.git
   cd salesforce-rag
2. Install Dependencies.
  openai>=1.0.0
  pinecone-client>=3.0.0
  langchain>=0.1.0
  streamlit>=1.25.0
  python-dotenv>=1.0.0
  numpy>=1.23.0
3. Prepare Environment Variables
   OPENAI_API_KEY=your-openai-api-key
   PINECONE_API_KEY=your-pinecone-api-key
   PINECONE_INDEX=salesforce-rag
4. Prepare Data
   Originally data is in pdf. Using script converted PDF file to .txt and placed in the /Data folder
5. Initialize Pinecone Index (First Time Only)
The ingest.py script will create the index if it does not exist.
6. Ingest and Index Transcripts
7. 7. Launch the Streamlit App
   
