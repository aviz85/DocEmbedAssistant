from database import Database
from embedding_service import EmbeddingService
from claude_service import ClaudeService

class SearchService:
    def __init__(self):
        self.db = Database()
        self.embedding_service = EmbeddingService()
        self.claude_service = ClaudeService()

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
        
        # Generate answer using Claude
        answer = self.claude_service.generate_response(query, formatted_results)
        
        return {
            'results': formatted_results,
            'answer': answer
        }
