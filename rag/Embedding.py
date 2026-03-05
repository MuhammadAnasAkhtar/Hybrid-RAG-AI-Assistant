from sentence_transformers import SentenceTransformer
from rag.Config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def embed_texts(texts):
    return model.encode(texts, show_progress_bar=True)

def embed_query(query):
    return model.encode([query])[0]