# RAG Chatbot Workflow Documentation

## Overview
This document explains how the RAG (Retrieval-Augmented Generation) Chatbot works and how all the files connect together.

## What is RAG?
RAG stands for **Retrieval-Augmented Generation**. Instead of the chatbot generating answers from its general knowledge, RAG:
1. **Retrieves** relevant information from your documents
2. **Augments** the user's question with that information
3. **Generates** an answer based on the retrieved context

This ensures the chatbot only answers from your provided documents, not general knowledge.

## Project Structure

```
workshop-chatbot/
├── main.py              # Entry point - orchestrates everything
├── config.py            # Configuration and API key management
├── document_loader.py    # Loads PDFs and CSVs
├── text_chunker.py      # Splits documents into chunks
├── embeddings.py        # Creates vector embeddings
├── vector_store.py      # Stores and searches chunks
├── rag_engine.py        # Main RAG logic
├── requirements.txt     # Python dependencies
├── .env.example         # Template for API key
└── WORKFLOW.md          # This file
```

## How Files Connect

### 1. **main.py** (The Orchestrator)
- **Imports**: All other modules
- **Role**: Main entry point that coordinates the entire workflow
- **Flow**:
  1. Loads config
  2. Calls document_loader to load files
  3. Calls text_chunker to split documents
  4. Calls embeddings to create vectors
  5. Calls vector_store to store everything
  6. Calls rag_engine to handle queries
  7. Runs the chat loop

### 2. **config.py** (Configuration Manager)
- **Imports**: os, dotenv
- **Role**: Manages settings and API keys
- **Used by**: All modules that need API key or settings
- **Provides**: API key, chunk size, model settings

### 3. **document_loader.py** (Document Processor)
- **Imports**: PDF library, pandas, os
- **Role**: Extracts text from PDFs and CSVs
- **Used by**: main.py
- **Returns**: Raw text from documents

### 4. **text_chunker.py** (Text Splitter)
- **Imports**: (minimal - basic Python)
- **Role**: Splits large documents into smaller chunks
- **Used by**: main.py
- **Why needed**: Large documents can't fit in one API call. Chunks allow:
  - Better processing
  - More precise retrieval
  - Efficient searching
- **Returns**: List of text chunks

### 5. **embeddings.py** (Vector Creator)
- **Imports**: google.generativeai, config
- **Role**: Converts text into numerical vectors (embeddings)
- **Used by**: main.py, rag_engine.py
- **Why needed**: 
  - Text can't be directly compared for similarity
  - Embeddings convert text to numbers that represent meaning
  - Similar texts have similar embeddings
- **Returns**: Embedding vectors (lists of numbers)

### 6. **vector_store.py** (Search Engine)
- **Imports**: embeddings (for similarity calculation)
- **Role**: Stores chunks and their embeddings, finds relevant chunks
- **Used by**: main.py, rag_engine.py
- **Why needed**:
  - Stores all document chunks
  - When user asks a question, finds the most relevant chunks
  - Uses similarity search (cosine similarity)
- **Returns**: Most relevant chunks for a query

### 7. **rag_engine.py** (The Brain)
- **Imports**: vector_store, embeddings, google.generativeai, config
- **Role**: Combines retrieval and generation
- **Used by**: main.py
- **Process**:
  1. Takes user question
  2. Converts question to embedding
  3. Searches vector_store for relevant chunks
  4. Creates a prompt with context + question
  5. Sends to Gemini API
  6. Returns answer
- **Returns**: Generated answer based on retrieved context

## Complete Workflow

### Initialization Phase (Document Ingestion)
```
User provides documents
    ↓
main.py calls document_loader.py
    ↓
document_loader.py extracts text from PDF/CSV
    ↓
main.py calls text_chunker.py
    ↓
text_chunker.py splits text into chunks
    ↓
main.py calls embeddings.py
    ↓
embeddings.py creates vector for each chunk
    ↓
main.py calls vector_store.py
    ↓
vector_store.py stores chunks + embeddings
```

### Query Phase (Answering Questions)
```
User asks a question
    ↓
main.py sends question to rag_engine.py
    ↓
rag_engine.py calls embeddings.py to embed question
    ↓
rag_engine.py calls vector_store.py to find relevant chunks
    ↓
vector_store.py returns top-k most similar chunks
    ↓
rag_engine.py creates prompt: context + question
    ↓
rag_engine.py sends prompt to Gemini API
    ↓
Gemini returns answer
    ↓
main.py displays answer to user
```

## Data Flow Example

Let's say you have a PDF about "Python Basics":

1. **Document Loading**: 
   - `document_loader.py` reads the PDF
   - Extracts: "Python is a programming language. It has variables, functions, and classes..."

2. **Chunking**:
   - `text_chunker.py` splits into:
     - Chunk 1: "Python is a programming language..."
     - Chunk 2: "It has variables, functions..."
     - Chunk 3: "Classes are used for..."

3. **Embedding**:
   - `embeddings.py` converts each chunk to a vector:
     - Chunk 1 → [0.1, 0.5, -0.3, ...]
     - Chunk 2 → [0.2, 0.4, -0.2, ...]
     - Chunk 3 → [0.15, 0.6, -0.25, ...]

4. **Storage**:
   - `vector_store.py` stores: {chunk_text: embedding_vector}

5. **Query**:
   - User asks: "What is Python?"
   - `rag_engine.py` embeds question: [0.12, 0.48, -0.28, ...]
   - `vector_store.py` finds Chunk 1 is most similar
   - `rag_engine.py` creates prompt:
     ```
     Context: "Python is a programming language..."
     Question: "What is Python?"
     ```
   - Gemini answers: "Based on the context, Python is a programming language."

## Key Concepts

### Why Chunking?
- Documents are too large for API calls
- Chunks allow precise retrieval (only relevant parts)
- Better performance and accuracy

### Why Embeddings?
- Convert text to numbers that represent meaning
- Similar texts = similar numbers
- Enables semantic search (finding meaning, not just keywords)

### Why Vector Store?
- Fast similarity search
- Finds relevant chunks quickly
- Stores everything in memory (simple approach)

### Why RAG?
- Answers only from your documents
- No hallucination (making up answers)
- Up-to-date information (your documents)
- Domain-specific knowledge

## Implementation Order

Students should implement in this order:
1. **config.py** - Get API key working
2. **document_loader.py** - Test loading a PDF/CSV
3. **text_chunker.py** - Test chunking text
4. **embeddings.py** - Test creating embeddings
5. **vector_store.py** - Test storing and searching
6. **rag_engine.py** - Test RAG query
7. **main.py** - Put it all together

## Testing Strategy

Test each module independently:
- Load a document → verify text extracted
- Chunk text → verify chunks created
- Create embeddings → verify vectors generated
- Store in vector store → verify storage works
- Search vector store → verify relevant chunks found
- RAG query → verify answer is from context

## Common Issues

1. **API Key not found**: Check .env file exists and has correct key
2. **No relevant chunks**: Chunk size might be too small/large
3. **Generic answers**: Prompt might not emphasize "only from context"
4. **Slow performance**: Too many chunks or inefficient search

## Next Steps

After completing the basic version, students can enhance:
- Support for more file types (Word, Excel, etc.)
- Better chunking strategies (sentence-aware)
- External vector database (Pinecone, Weaviate)
- Chat history
- Web interface
- Better error handling

