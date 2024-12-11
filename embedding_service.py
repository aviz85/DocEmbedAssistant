import cohere
import numpy as np
import os

class EmbeddingService:
    def __init__(self):
        self.co = cohere.Client(os.environ.get('COHERE_API_KEY'))
        self.model = "embed-english-v3.0"  # Using v3.0 model with 1024 dimensions

    def get_embeddings(self, texts, batch_size=96):
        """Get embeddings for a list of texts, processing in batches"""
        all_embeddings = []
        
        # Process in batches of 96 (Cohere's limit)
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            try:
                response = self.co.embed(
                    texts=batch,
                    model=self.model,
                    input_type='search_document'
                )
                embeddings = response.embeddings
                all_embeddings.extend(embeddings)
            except Exception as e:
                print(f"Error getting embeddings for batch: {e}")
                # Return empty embeddings for failed batch
                all_embeddings.extend([np.zeros(1024) for _ in batch])
        
        return np.array(all_embeddings)

    def get_query_embedding(self, query):
        """Get embedding for a search query"""
        try:
            response = self.co.embed(
                texts=[query],
                model=self.model,
                input_type='search_query'
            )
            return np.array(response.embeddings[0])
        except Exception as e:
            print(f"Error getting query embedding: {e}")
            return np.zeros(1024)
