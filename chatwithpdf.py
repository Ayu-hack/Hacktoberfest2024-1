from pypdf import PdfReader
import openai
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pgvector.sqlalchemy import Vector
import numpy as np

# Constants
N_DIM = 1536
openai.api_key = 'your_openai_api_key'

# SQLAlchemy setup
Base = declarative_base()

class TextEmbedding(Base):
    __tablename__ = 'text_embeddings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String)
    embedding = Vector(N_DIM)

# Database connection
engine = create_engine('postgresql://user:password@localhost/dbname')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def read_pdf(file_path):
    pdf_reader = PdfReader(file_path)
    text = ""
    for page in pdf_reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text + "\n"
    return text

def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    end = 0
    while end < len(text):
        end = start + chunk_size
        if end > len(text):
            end = len(text)
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def generate_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        response = openai.Embedding.create(
            input=chunk,
            model="text-embedding-ada-002"
        )
        embeddings.append(response['data'][0]['embedding'])
    return embeddings

def insert_embeddings(embeddings):
    for embedding in embeddings:
        new_embedding = TextEmbedding(embedding=embedding)
        session.add(new_embedding)
    session.commit()

def find_similar_embeddings(query_embedding, limit=5):
    k = 5
    similarity_threshold = 0.7
    query = session.query(TextEmbedding, TextEmbedding.embedding.cosine_distance(query_embedding)
            .label("distance"))
            .filter(TextEmbedding.embedding.cosine_distance(query_embedding) < similarity_threshold)
            .order_by("distance")
            .limit(k)
            .all()
    return query

if __name__ == "__main__":
    # Example usage
    pdf_text = read_pdf("path_to_your_pdf.pdf")
    text_chunks = split_text(pdf_text)
    embeddings = generate_embeddings(text_chunks)
    insert_embeddings(embeddings)
    
    # Example query (you would need to generate a query embedding first)
    # query_embedding = generate_embeddings(["Your query text"])[0]
    # similar_embeddings = find_similar_embeddings(query_embedding)
    # Process and use similar_embeddings as needed
