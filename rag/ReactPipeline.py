from rag.PDFLoader import load_pdfs
from rag.Chunking import chunk_text
from rag.Embedding import embed_texts, embed_query
from rag.VectorStore import VectorStore
from rag.BM25Retriever import BM25Retriever
from rag.Rerank import rerank
from rag.Config import TOP_K

class HybridRAG:

    def __init__(self):
        self.vector_store = None
        self.bm25 = None
        self.chunks = []

    def build(self):

        documents = load_pdfs()

        if not documents:
            print("No PDFs found.")
            return

        self.chunks = []

        for doc in documents:
            self.chunks.extend(chunk_text(doc))

        embeddings = embed_texts(self.chunks)

        self.vector_store = VectorStore(len(embeddings[0]))
        self.vector_store.add(embeddings, self.chunks)

        self.bm25 = BM25Retriever(self.chunks)

        print("Hybrid RAG Ready!")

    def retrieve(self, query):

        if not self.vector_store:
            return ["Upload a PDF first."]

        dense = self.vector_store.search(embed_query(query), TOP_K)
        sparse = self.bm25.search(query, TOP_K)

        combined = list(set(dense + sparse))

        return rerank(query, combined, TOP_K)