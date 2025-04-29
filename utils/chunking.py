import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_transcripts(input_folder, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = []
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                chunks = splitter.split_text(text)
                docs.extend([{'text': chunk, 'source': filename} for chunk in chunks])
    return docs
