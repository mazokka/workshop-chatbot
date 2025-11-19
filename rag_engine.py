"""
RAG Engine Module

This is the main RAG (Retrieval-Augmented Generation) engine that combines retrieval and generation

TODO:
1. Import necessary modules:
   - vector_store (for retrieving relevant chunks)
   - embeddings (for creating query embeddings)
   - google.generativeai (for generating responses)
   - config (for API key and settings)

2. Create a RAGEngine class or functions:
   - Initialize with vector_store and Gemini client
   - Set up Gemini API with API key from config

3. Create a query method:
   - Takes a user question as input
   - Step 1: Convert the question to an embedding (using embeddings module)
   - Step 2: Search vector_store for most relevant chunks (top 3-5)
   - Step 3: Combine the retrieved chunks into context
   - Step 4: Create a prompt that includes:
     - Instructions to only answer from the provided context
     - The retrieved context/chunks
     - The user's question
   - Step 5: Send prompt to Gemini API
   - Step 6: Return the generated response

4. Prompt engineering:
   - Make sure the prompt tells the model to ONLY use information from context
   - If the answer isn't in the context, it should say "I don't have that information"
   - Format the context nicely for the model to understand

5. Error handling:
   - Handle API errors
   - Handle cases where no relevant chunks are found
"""

