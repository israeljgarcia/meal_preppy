from flask import Blueprint

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/')
def index():
    return "User route"
