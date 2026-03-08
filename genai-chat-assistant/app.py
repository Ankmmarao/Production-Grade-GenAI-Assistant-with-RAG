from flask import Flask, render_template, request, jsonify
import json
import google.generativeai as genai

app = Flask(__name__)

# Add your Gemini API Key
genai.configure(api_key="")

model = genai.GenerativeModel("models/gemini-2.5-flash")

# Load documents
with open("docs.json", "r") as f:
    documents = json.load(f)

# Combine documents as context
def get_context():

    context = ""

    for doc in documents:
        context += doc["title"] + ": " + doc["content"] + "\n"

    return context


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    context = get_context()

    prompt = f"""
You are a helpful assistant.

Use the following information to answer the user.

Context:
{context}

Question:
{user_message}
"""

    response = model.generate_content(prompt)

    return jsonify({"reply": response.text})


if __name__ == "__main__":
    app.run(debug=True)
