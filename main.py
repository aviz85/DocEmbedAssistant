import streamlit as st
import os
from document_processor import DocumentProcessor
from embedding_service import EmbeddingService
from search_service import SearchService
from database import Database

# Initialize services
doc_processor = DocumentProcessor()
embedding_service = EmbeddingService()
search_service = SearchService()
db = Database()

def process_uploaded_file(file):
    try:
        # Read text content
        text_content = file.getvalue().decode('utf-8')
        
        # Process document into chunks
        chunks = doc_processor.process_text(text_content)
        
        # Get embeddings for chunks
        with st.spinner('Generating embeddings...'):
            embeddings = embedding_service.get_embeddings(chunks)
        
        # Store in database
        with st.spinner('Storing document...'):
            db.store_document_chunks(file.name, chunks, embeddings)
        
        st.success(f'Successfully processed {file.name}')
        return True
    except Exception as e:
        st.error(f'Error processing file: {str(e)}')
        return False

def main():
    st.title('Document Q&A System')
    
    # Sidebar with file upload
    with st.sidebar:
        st.header('Upload Documents')
        uploaded_file = st.file_uploader("Choose a text file", type=['txt'])
        
        if uploaded_file is not None:
            if st.button('Process Document'):
                process_uploaded_file(uploaded_file)
        
        st.header('Available Documents')
        documents = db.get_all_documents()
        for doc in documents:
            st.text(doc)
    
    # Main area for search
    st.header('Ask a Question')
    query = st.text_input('Enter your question:')
    
    if query:
        with st.spinner('Searching...'):
            results = search_service.search(query)
        
        st.header('Search Results')
        for i, result in enumerate(results, 1):
            with st.container():
                st.markdown(f"**Result {i}** (Similarity: {result['similarity']}%)")
                st.markdown(f"*From: {result['filename']}*")
                st.text(result['content'])
                st.markdown("---")

if __name__ == "__main__":
    main()
