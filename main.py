"""
Main Application File

This is the entry point of the RAG Chatbot application.

TODO:
1. Import all necessary modules:
   - document_loader
   - text_chunker
   - embeddings
   - vector_store
   - rag_engine
   - config

2. Create the main workflow:
   - Step 1: Load configuration and validate API key
   - Step 2: Ask user for document path(s) or directory
   - Step 3: Load documents using document_loader
   - Step 4: Chunk the documents using text_chunker
   - Step 5: Generate embeddings for chunks using embeddings module
   - Step 6: Store chunks and embeddings in vector_store
   - Step 7: Initialize RAG engine with the vector_store
   - Step 8: Start a chat loop:
     - Ask user for a question
     - Use RAG engine to get answer
     - Display the answer
     - Continue until user types 'exit' or 'quit'

3. User interface:
   - Simple command-line interface
   - Clear prompts and messages
   - Show loading messages during document processing

4. Error handling:
   - Handle file not found errors
   - Handle API errors
   - Handle invalid inputs

5. Optional enhancements:
   - Allow loading multiple documents
   - Show which document the answer came from
   - Save chat history
"""

