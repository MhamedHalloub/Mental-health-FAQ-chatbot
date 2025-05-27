from flask import Flask, request, render_template
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load and prepare data
df = pd.read_csv("Mental_Health_FAQ.csv")
questions = df['Questions'].tolist()
answers = df['Answers'].tolist()

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

processed_questions = [preprocess(q) for q in questions]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

def get_answer(user_query):
    processed_query = preprocess(user_query)
    query_vec = vectorizer.transform([processed_query])
    similarity = cosine_similarity(query_vec, X)
    best_match_idx = similarity.argmax()
    best_score = similarity[0, best_match_idx]
    if best_score < 0.2:
        return "I'm sorry, I couldn't find an answer. Please rephrase your question."
    return answers[best_match_idx]

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_query = request.form.get("question")
        response = get_answer(user_query)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
