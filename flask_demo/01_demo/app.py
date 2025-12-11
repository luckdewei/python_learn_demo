from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "欢迎来到 Flask 基础课程！"


@app.route("/user/<username>")
def show_user_profile(username):
    return f"用户: {username}"


if __name__ == "__main__":
    app.run(debug=True)
