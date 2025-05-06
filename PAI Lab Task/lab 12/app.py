from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np

app = Flask(__name__)

# Load data and create index once
def initialize_bot():
    df = pd.read_csv('medical_data.csv')
    questions = df['question'].tolist()
    answers = df['answer'].tolist()

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(questions, convert_to_numpy=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return model, answers, index

model, answers, index = initialize_bot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]
    user_embedding = model.encode([user_msg], convert_to_numpy=True)
    _, I = index.search(user_embedding, k=1)
    best_match_index = int(I[0][0])
    response = answers[best_match_index]
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

