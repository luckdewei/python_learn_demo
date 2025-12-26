from flask import Flask, request
from views.user import user_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)

    @app.before_request
    def before():
        print("请求:", request.method, request.path)

    @app.errorhandler(404)
    def not_found(e):
        return {"msg": "not found"}, 404

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
