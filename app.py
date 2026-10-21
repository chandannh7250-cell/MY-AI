from flask import Flask, request, jsonify
from myai_library.engine import generate_code, search_code

app = Flask(__name__)

@app.route("/")
def home():
    return "MY-AI is Live! Use /ask?prompt=hello"

@app.route("/ask")
def ask():
    prompt = request.args.get("prompt", "")
    result = generate_code(prompt)
    if not result:
        result = search_code(prompt)
    return jsonify({"prompt": prompt, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
from flask import Flask, request, jsonify, render_template_string
from myai_library.engine import generate_code, search_code

app = Flask(__name__)

HTML = """
<html>
<head><title>MY-AI</title>
<style>
body{font-family:Arial; text-align:center; background:#f0f0f0; padding:20px;}
input{width:85%; padding:12px; font-size:18px; border-radius:10px; border:1px solid #ccc;}
button{padding:12px 25px; font-size:18px; background:#007bff; color:white; border:none; border-radius:10px; margin-top:10px;}
.box{background:white; padding:20px; border-radius:15px; margin-top:20px; text-align:left;}
</style>
</head>
<body>
<h2>🤖 MY-AI - Input / Output / Code</h2>
<form method="POST">
<input type="text" name="prompt" placeholder="Yahan likho: hello ya table of 7" required>
<br><button type="submit">Bhejo</button>
</form>
{% if result %}
<div class="box">
<h3>✅ Input: {{ user_input }}</h3>
<h3>👉 Output:</h3>
<pre>{{ result }}</pre>
<h3>💻 Code:</h3>
<pre>{{ result }}</pre>
</div>
{% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET','POST'])
def home():
    result = ""
    user_input = ""
    if request.method == 'POST':
        user_input = request.form.get("prompt","")
        result = generate_code(user_input)
        if not result:
            result = search_code(user_input)
        if not result:
            result = "Result nahi mila"
    return render_template_string(HTML, result=result, user_input=user_input)

@app.route('/ask')
def ask():
    prompt = request.args.get("prompt", "")
    result = generate_code(prompt)
    if not result:
        result = search_code(prompt)
    return jsonify({"prompt": prompt, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
