from flask import Flask, request, render_template_string
from myai_library.engine import generate_code, run_code

app = Flask(__name__)

HTML = """
<html><head><title>MY-AI Calculator</title></head>
<body style="background:#f2f2f2; font-family:Arial; text-align:center; padding:20px;">
<h2>🤖 MY-AI - Calculator + Code</h2>

<div style="background:white; padding:15px; border-radius:10px; margin-bottom:15px;">
<button onclick="document.querySelector('input[name=prompt]').value='5+5'">5+5</button>
<button onclick="document.querySelector('input[name=prompt]').value='10*5'">10*5</button>
<button onclick="document.querySelector('input[name=prompt]').value='100/4'">100/4</button>
<button onclick="document.querySelector('input[name=prompt]').value='table of 5'">Table of 5</button>
</div>

<form method="POST">
<input type="text" name="prompt" value="{{ user_input }}" placeholder="Likho: 5+5 ya table of 5" style="width:95%; padding:12px; border-radius:8px;" required>
<input type="hidden" name="action" value="get_code">
</form>
<p style="font-size:12px; color:#888;">Enter dabao, Code aayega</p>

{% if code %}
<div style="background:white; padding:15px; border-radius:10px; text-align:left;">
<h3>✅ Input: {{ user_input }}</h3>
<h3>💻 Code:</h3>
<pre>{{ code }}</pre>
<form method="POST">
<input type="hidden" name="prompt" value="{{ user_input }}">
<input type="hidden" name="code" value="{{ code }}">
<input type="hidden" name="action" value="run">
<button type="submit" style="background:green; color:white; padding:10px 20px; border:none; border-radius:8px;">▶ Run / Answer</button>
</form>
{% if result %}
<h3>👉 Output / Result:</h3>
<pre style="background:#e8ffe8; padding:10px; border-radius:5px; font-size:20px;">{{ result }}</pre>
{% endif %}
</div>
{% endif %}
</body></html>
"""

@app.route('/', methods=['GET','POST'])
def home():
    user_input = ""
    code = ""
    result = ""
    if request.method == 'POST':
        action = request.form.get("action")
        user_input = request.form.get("prompt","")
        if action == "get_code":
            code = generate_code(user_input)
        elif action == "run":
            code = request.form.get("code","")
            result = run_code(code)
    return render_template_string(HTML, user_input=user_input, code=code, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
