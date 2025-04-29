import streamlit as st
from utils.retrieval import retrieve_top_k
from utils.embedding import generate_answer
from dotenv import load_dotenv

load_dotenv()

st.title("Salesforce Earnings Call Q&A Assistant (Pinecone)")
query = st.text_input("Ask a question or request a summary:")

if st.button("Submit") and query:
    with st.spinner("Retrieving answer..."):
        context_chunks = retrieve_top_k(query)
        answer = generate_answer(query, context_chunks)
        st.write("**Answer:**")
        st.write(answer)
        st.write("---")
        st.write("**Context Chunks Used:**")
        for chunk in context_chunks:
            st.write(f"- Source: {chunk['source']}")
            st.write(chunk['text'][:300] + "...")
