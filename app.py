from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

from rag.ReactPipeline import HybridRAG
from rag.LLM import generate_answer
from rag.Config import PDF_FOLDER, ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = PDF_FOLDER

os.makedirs(PDF_FOLDER, exist_ok=True)

rag = HybridRAG()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"})

    file = request.files["file"]

    if file and "." in file.filename and file.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        rag.build()

        return jsonify({"message": "PDF uploaded and indexed successfully!"})

    return jsonify({"error": "Invalid file"})


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query")

    docs = rag.retrieve(query)
    answer = generate_answer(query, docs)

    utc_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    return jsonify({
        "answer": answer,
        "time": utc_time
    })


if __name__ == "__main__":
    app.run(debug=True)