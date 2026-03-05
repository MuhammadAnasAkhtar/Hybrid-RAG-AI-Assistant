from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self, documents):
        self.documents = documents
        tokenized = [doc.split() for doc in documents]
        self.bm25 = BM25Okapi(tokenized)

    def search(self, query, top_k):
        return self.bm25.get_top_n(query.split(), self.documents, n=top_k)