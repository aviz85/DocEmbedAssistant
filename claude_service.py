import anthropic
import os
from typing import List, Dict

class ClaudeService:
    def __init__(self):
        self.client = anthropic.Client(api_key=os.environ['ANTHROPIC_API_KEY'])
        self.model = "claude-3-sonnet-20240229"
        self.max_tokens = 1024
        
    def generate_response(self, query: str, search_results: List[Dict]) -> str:
        """Generate a response using Claude based on the search results"""
        # Format the context from search results
        context = "\n\n".join([
            f"Content from {result['filename']}:\n{result['content']}"
            for result in search_results
        ])
        
        # Create the system prompt
        system_prompt = """You are a helpful assistant that answers questions based on the provided document context. 
        Always cite the source documents in your response. If the context doesn't contain enough information to answer 
        the question, say so clearly."""
        
        # Create the user message with context
        user_message = f"""Context from relevant documents:
        {context}
        
        Question: {query}
        
        Please provide a clear and concise answer based on the context above."""
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=0.7,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}]
            )
            return response.content[0].text
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Sorry, I encountered an error while generating the response. Please try again."
