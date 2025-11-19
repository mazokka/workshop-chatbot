# RAG Chatbot Workshop

A simple RAG (Retrieval-Augmented Generation) chatbot that answers questions based on your documents (PDFs and CSVs).

## Project Overview

This project implements a basic RAG chatbot that:
- Ingests documents (PDF or CSV files)
- Splits them into manageable chunks
- Creates embeddings for semantic search
- Answers questions based only on the provided documents

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key

### 3. Configure Environment

1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Open `.env` and add your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 4. Add Your Documents

Create a `documents/` folder and add your PDF or CSV files there.

### 5. Run the Application

```bash
python main.py
```

## Project Structure

- `main.py` - Entry point, orchestrates the workflow
- `config.py` - Configuration and API key management
- `document_loader.py` - Loads and processes PDF/CSV files
- `text_chunker.py` - Splits documents into chunks
- `embeddings.py` - Creates vector embeddings
- `vector_store.py` - Stores and searches document chunks
- `rag_engine.py` - Main RAG logic (retrieval + generation)
- `WORKFLOW.md` - Detailed explanation of how everything works

## How to Use

1. Run `python main.py`
2. Provide the path to your document(s) when prompted
3. Wait for the documents to be processed
4. Ask questions about your documents
5. Type 'exit' or 'quit' to end the session

## Learning Objectives

By completing this project, you will learn:
- How RAG (Retrieval-Augmented Generation) works
- Document processing and chunking
- Vector embeddings and similarity search
- Integrating with LLM APIs (Gemini)
- Building a complete AI application

## Implementation Guide

Each file contains detailed TODO comments explaining what needs to be implemented. Start with `config.py` and work through the files in this order:

1. `config.py`
2. `document_loader.py`
3. `text_chunker.py`
4. `embeddings.py`
5. `vector_store.py`
6. `rag_engine.py`
7. `main.py`

See `WORKFLOW.md` for detailed explanations of how each component works and how they connect together.

## Notes

- This is a basic implementation using in-memory storage
- No external database is required
- All embeddings and chunks are stored in memory
- Perfect for learning and small-scale use

## Troubleshooting

- **API Key Error**: Make sure `.env` file exists and contains `GEMINI_API_KEY`
- **Module Not Found**: Run `pip install -r requirements.txt`
- **File Not Found**: Check that your document path is correct
