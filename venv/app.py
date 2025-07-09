from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)

OPENROUTER_API_KEY = "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"

def convert_code_blocks(text):
    # Ganti blok kode triple backtick dengan tag HTML <pre><code>
    code_pattern = re.compile(r"```(\w+)?\n(.*?)```", re.DOTALL)
    return code_pattern.sub(
        lambda m: f"<pre><code class='language-{m.group(1) or 'plaintext'}'>{m.group(2).strip()}</code></pre>",
        text
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json.get("prompt", "").strip()

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "chatbot-smk"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        reply_html = convert_code_blocks(reply)
    except Exception as e:
        reply_html = "Maaf, terjadi kesalahan atau limit penggunaan telah habis."

    return jsonify({"reply": reply_html})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
