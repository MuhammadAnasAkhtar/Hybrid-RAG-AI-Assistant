from sentence_transformers import CrossEncoder
from rag.Config import RERANK_MODEL

reranker = CrossEncoder(RERANK_MODEL)

def rerank(query, documents, top_k):
    pairs = [(query, doc) for doc in documents]
    scores = reranker.predict(pairs)

    ranked = sorted(zip(documents, scores),
                    key=lambda x: x[1],
                    reverse=True)

    return [doc for doc, score in ranked[:top_k]]