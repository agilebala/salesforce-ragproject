import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text):
    return openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )['data'][0]['embedding']

def generate_answer(query, context_chunks):
    context = "\n\n".join(chunk['text'] for chunk in context_chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for Salesforce earnings calls."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
