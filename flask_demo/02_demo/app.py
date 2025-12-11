from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit_form():
    username = request.form["username"]
    return f"你好呀, {username}!"


if __name__ == "__main__":
    app.run(
        debug=True
    )  ##cd /workspace/flask_basics 然后执行python app.py打开web预览查看效果tenpl
