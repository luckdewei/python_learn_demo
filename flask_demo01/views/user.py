from flask import Blueprint, request
from models.user import UserModel
from utils.response import success, error

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.get("/")
def list_users():
    return success(UserModel.get_all())


@user_bp.post("/")
def create_user():
    data = request.json
    if not data:
        return error("invalid json")

    name = data.get("name")
    age = data.get("age")

    if not name:
        return error("name required")

    UserModel.create(name, age)
    return success()
