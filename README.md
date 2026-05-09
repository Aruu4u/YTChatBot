# YTChatBot

A YouTube chatbot project built using Python, LangChain, Ollama, FAISS, and Hugging Face embeddings.

This project allows you to:
- Load and process YouTube transcripts
- Create embeddings from transcript data
- Store embeddings using FAISS
- Ask questions from YouTube video content
- Run the chatbot locally using Ollama Llama 3.3 model

---

# Requirements

## Install Python
Make sure you have Python 3.11+ installed.

Check version:

```bash
python --version
```

---

# Create Virtual Environment

```bash
python -m venv ytbotenv
```

Activate virtual environment:

## Windows

```bash
ytbotenv\Scripts\activate
```

## Linux / Mac

```bash
source ytbotenv/bin/activate
```

---

# Install Required Libraries

Install all dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install langchain
pip install langchain-community
pip install langchain-core
pip install langchain-ollama
pip install langchain-huggingface
pip install faiss-cpu
pip install sentence-transformers
pip install python-dotenv
pip install youtube-transcript-api
pip install pypdf
pip install tiktoken
pip install torch
pip install transformers
```

---

# Install Ollama

Download and install Ollama:

https://ollama.com/download

After installation verify:

```bash
ollama --version
```

---

# Pull Required Ollama Model

This project uses Llama 3.2.

Run:

```bash
ollama pull llama3.2
```

---

# Start Ollama Server

Make sure Ollama is running in the background.

Run:

```bash
ollama run llama3.2
```

Keep this terminal running.

---

# Hugging Face Token Setup

Create a `.env` file in the root directory.

Add:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

Get token from:

https://huggingface.co/settings/tokens

IMPORTANT:
- Never upload `.env` to GitHub
- Keep your token private

---

# Run the Project

Run the chatbot:

```bash
python YTchatbot_1.py
```

---

# Project Structure

```text
YTChatBot/
│
├── YTchatbot_1.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── vectorstore/
```

---

# Features

- YouTube transcript loading
- Vector database using FAISS
- Hugging Face embeddings
- Local LLM using Ollama
- Retrieval-Augmented Generation (RAG)
- Chat with YouTube videos

---

# Important Notes

## Do NOT upload these folders/files to GitHub

```text
ytbotenv/
venv/
__pycache__/
.env
```

---

# Generate requirements.txt

If you install additional libraries:

```bash
pip freeze > requirements.txt
```

---

# Common Errors

## Ollama model not found

Run:

```bash
ollama pull llama3.3
```

---

## Ollama server not running

Start Ollama:

```bash
ollama run llama3.3
```

---

## ModuleNotFoundError

Install missing package:

```bash
pip install package_name
```

Example:

```bash
pip install langchain-ollama
```

---

# Future Improvements

- Add Streamlit UI
- Add Chrome Extension
- Add chat memory
- Add multi-video support
- Add voice input
- Deploy on cloud

---

# Author

Arsal Masood

