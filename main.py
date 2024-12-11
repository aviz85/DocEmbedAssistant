import streamlit as st
import os
from document_processor import DocumentProcessor
from embedding_service import EmbeddingService
from search_service import SearchService
from database import Database
from tts_service import TTSService

# Initialize services
doc_processor = DocumentProcessor()
embedding_service = EmbeddingService()
search_service = SearchService()
db = Database()

def process_uploaded_file(file):
    try:
        # Process document into chunks
        chunks = doc_processor.process_file(file)
        
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
        uploaded_file = st.file_uploader("Choose a file", type=['txt', 'pdf', 'docx'])
        
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
        with st.spinner('Searching and generating answer...'):
            response = search_service.search(query)
            
        # Display generated answer
        st.header('Answer')
        answer_text = response['answer']
        st.write(answer_text)
        
        # Add text-to-speech button
        if st.button('🔊 Play Answer'):
            with st.spinner('Generating speech...'):
                tts = TTSService()
                audio_data = tts.text_to_speech(answer_text)
                if audio_data:
                    st.audio(f"data:audio/mp3;base64,{audio_data}", format='audio/mp3')
                else:
                    st.error('Failed to generate speech')
        
        # Display supporting search results
        st.header('Supporting Documents')
        for i, result in enumerate(response['results'], 1):
            with st.container():
                st.markdown(f"**Result {i}** (Similarity: {result['similarity']}%)")
                st.markdown(f"*From: {result['filename']}*")
                st.text(result['content'])
                st.markdown("---")

if __name__ == "__main__":
    main()
