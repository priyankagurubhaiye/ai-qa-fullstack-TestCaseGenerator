from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    file = request.files["file"]
    content = file.read().decode("utf-8")

    prompt = f"""
    You are a QA expert. Generate test cases including:
    - Positive
    - Negative
    - Edge cases

    Requirement:
    {content}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content
    return jsonify({"testcases": result})

if __name__ == "__main__":
    app.run(debug=True)
