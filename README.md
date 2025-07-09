# 📄 rag-pdf-chatbot

A PDF-powered chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer user questions based on content from any uploaded PDF. Built using **LangChain**, **Hugging Face Transformers**, **ChromaDB**, and **Streamlit** — all running locally without any API tokens.

---

## 🧠 Features

- 📄 Upload any PDF file
- 🤖 Ask natural language questions
- 🔍 Uses vector embeddings + local language model
- 🧠 Built on `flan-t5-base` (runs locally using Hugging Face pipeline)
- 💬 Answers in English (even if PDF is in another language)
- 🛠 100% private and offline (no API key needed)

---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/risingstar21/rag-pdf-chatbot.git
cd rag-pdf-chatbot
2. Set up virtual environment (recommended)
bash
Copy
Edit
python -m venv venv
venv\\Scripts\\activate    # on Windows
# or
source venv/bin/activate   # on Mac/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
streamlit run app.py
🛠 Tech Stack
Tool	Description
Streamlit	Interactive UI
LangChain	Handles retrieval + LLM chaining
Hugging Face Transformers	Model: flan-t5-base
ChromaDB	Lightweight vector store
Sentence Transformers	Embeddings using all-MiniLM-L6-v2
PDFMiner	PDF reading and text extraction

📂 Folder Structure
css
Copy
Edit
rag-pdf-chatbot/
├── app.py                ← Main chatbot code
├── requirements.txt      ← Python dependencies
├── .gitignore            ← Ignore venv, db, etc.
└── README.md             ← This file!
📸 Preview (Optional)
💡 Add a screenshot of your Streamlit chatbot UI here
You can press Win + Shift + S to take a screenshot
Then upload it and paste markdown like:
![Chatbot Screenshot](screenshot.png)

📄 License
This project is licensed under the MIT License — feel free to use, modify, and share.

🙌 Author
Made with ❤️ by risingstar21

⭐ Like This?
If you found this useful, give it a ⭐ on GitHub and share it with others!
