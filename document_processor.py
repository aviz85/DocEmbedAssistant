import re

class DocumentProcessor:
    def __init__(self, chunk_size=1000, chunk_overlap=100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def clean_text(self, text):
        # Remove multiple newlines and whitespace
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def split_into_chunks(self, text):
        text = self.clean_text(text)
        chunks = []
        
        start = 0
        while start < len(text):
            # Find a good breaking point
            end = start + self.chunk_size
            if end < len(text):
                # Try to break at a sentence or paragraph
                break_chars = ['.', '!', '?', '\n']
                for char in break_chars:
                    last_break = text.rfind(char, start, end)
                    if last_break != -1:
                        end = last_break + 1
                        break
            
            chunk = text[start:end].strip()
            if chunk:  # Only add non-empty chunks
                chunks.append(chunk)
            
            # Move start position for next chunk, accounting for overlap
            start = end - self.chunk_overlap
            if start < 0:
                start = 0
        
        return chunks

    def process_text(self, text):
        """Process a text document and return chunks"""
        return self.split_into_chunks(text)
