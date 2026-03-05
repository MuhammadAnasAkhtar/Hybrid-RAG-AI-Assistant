import ollama
from rag.Config import OLLAMA_MODEL

def generate_answer(query, context_docs):
    context = "\n\n".join(context_docs)

    prompt = f"""
Use ONLY the context below to answer.

Context:
{context}

Question:
{query}

Answer:
"""

    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Model Error: {e}"