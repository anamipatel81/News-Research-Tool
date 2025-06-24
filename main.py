import os
import streamlit as st
import pickle
import time

from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Streamlit UI
st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_ollama.pkl"

main_placeholder = st.empty()

# Load local LLM (e.g. mistral or llama3 via Ollama)
llm = Ollama(model="mistral")  # or use model="llama3"

if process_url_clicked:
    # Load data from URLs
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)

    # Generated embeddings using a local model (via HuggingFace)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(1)

    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)

# Query section
query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
            result = qa_chain.run(query)
            st.header("Answer")
            st.write(result)

            # Display source if available
            sources = result.get("sources", None) or result.get("metadata", {}).get("source_url", "")

            if sources:
                st.subheader("Sources:")
                if isinstance(sources, str):
                    st.write(sources)  # If it's a string, display directly
                elif isinstance(sources, list):
                    for source in sources:  # If it's a list, display each item
                        st.write(source)
            else:
                st.warning("No sources available.")
