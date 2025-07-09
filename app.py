import streamlit as st
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain import HuggingFacePipeline
from transformers import pipeline
import os

st.title("📄 Audi Car PDF Chatbot")
st.write("Upload a PDF and ask questions based on its content.")

uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file is not None:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully!")

    try:
        loader = PyPDFLoader("uploaded.pdf")
        pages = loader.load()
        st.info(f"📄 Total pages loaded: {len(pages)}")

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.split_documents(pages)
        st.info(f"📚 Total chunks created: {len(docs)}")

        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        db = Chroma.from_documents(docs, embeddings, persist_directory="db")
        retriever = db.as_retriever()

        # ✅ No token needed — local model runs free
        hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", max_length=100)
        llm = HuggingFacePipeline(pipeline=hf_pipeline)

        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        query = st.text_input("Please ask a question:")

        if query:
            with st.spinner("🔍 Thinking..."):
                # Force English in prompt
                english_prompt = f"Answer in English only. {query}"
                answer = qa_chain.run(english_prompt)
            st.success(f"🧠 Your Answer: {answer}")

    except Exception as e:
        st.error(f"❌ Error: {e}")
