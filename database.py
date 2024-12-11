import os
import psycopg2
from psycopg2.extras import execute_values
import numpy as np

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.environ['PGHOST'],
            database=os.environ['PGDATABASE'],
            user=os.environ['PGUSER'],
            password=os.environ['PGPASSWORD'],
            port=os.environ['PGPORT']
        )
        self.setup_database()

    def setup_database(self):
        with self.conn.cursor() as cur:
            # Enable vector extension
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            
            # Create documents table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id SERIAL PRIMARY KEY,
                    filename TEXT NOT NULL,
                    content TEXT NOT NULL,
                    chunk_index INTEGER NOT NULL,
                    embedding vector(1024)
                );
            """)
            
            # Create index for vector similarity search
            cur.execute("""
                CREATE INDEX IF NOT EXISTS documents_embedding_idx 
                ON documents 
                USING hnsw (embedding vector_cosine_ops);
            """)
            
        self.conn.commit()

    def store_document_chunks(self, filename, chunks, embeddings):
        with self.conn.cursor() as cur:
            data = [
                (filename, chunk, idx, embedding.tolist())
                for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings))
            ]
            execute_values(
                cur,
                """
                INSERT INTO documents (filename, content, chunk_index, embedding)
                VALUES %s
                """,
                data,
                template="(%s, %s, %s, %s)"
            )
        self.conn.commit()

    def search_similar(self, query_embedding, limit=5):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT filename, content, chunk_index, 
                       1 - (embedding <=> %s) as similarity
                FROM documents
                ORDER BY embedding <=> %s
                LIMIT %s;
                """,
                (query_embedding.tolist(), query_embedding.tolist(), limit)
            )
            results = cur.fetchall()
        return [
            {
                'filename': r[0],
                'content': r[1],
                'chunk_index': r[2],
                'similarity': r[3]
            }
            for r in results
        ]

    def get_all_documents(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT DISTINCT filename FROM documents;")
            return [r[0] for r in cur.fetchall()]
