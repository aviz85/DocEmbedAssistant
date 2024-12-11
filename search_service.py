from database import Database
from embedding_service import EmbeddingService

class SearchService:
    def __init__(self):
        self.db = Database()
        self.embedding_service = EmbeddingService()

    def search(self, query, limit=5):
        # Get query embedding
        query_embedding = self.embedding_service.get_query_embedding(query)
        
        # Search database for similar documents
        results = self.db.search_similar(query_embedding, limit)
        
        # Format results
        formatted_results = []
        for result in results:
            formatted_results.append({
                'filename': result['filename'],
                'content': result['content'],
                'similarity': round(result['similarity'] * 100, 2),
                'chunk_index': result['chunk_index']
            })
        
        return formatted_results
