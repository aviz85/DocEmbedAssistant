import re
from docx import Document
from PyPDF2 import PdfReader
import io

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

    def read_pdf(self, file_content):
        """Extract text from PDF file"""
        pdf_reader = PdfReader(io.BytesIO(file_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text

    def read_docx(self, file_content):
        """Extract text from DOCX file"""
        doc = Document(io.BytesIO(file_content))
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text

    def process_file(self, file):
        """Process a file and return chunks"""
        content = file.getvalue()
        
        if file.name.lower().endswith('.pdf'):
            text = self.read_pdf(content)
        elif file.name.lower().endswith('.docx'):
            text = self.read_docx(content)
        elif file.name.lower().endswith('.txt'):
            text = content.decode('utf-8')
        else:
            raise ValueError("Unsupported file format. Please upload a PDF, DOCX, or TXT file.")
            
        return self.split_into_chunks(text)
