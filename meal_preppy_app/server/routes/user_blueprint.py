import jwt
import datetime
from functools import wraps
from flask import Blueprint, json, jsonify, request, redirect, session
from models.User import User
from models.Shared import db
from models.Pantry import Pantry
from config import jwt_key
user_blueprint = Blueprint('users', __name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        token = token.split(' ')

        token = token[1]

        if not token:
            return jsonify({'message': 'Token is missing'})

        try:
            data = jwt.decode(token, jwt_key, algorithms="HS256")
        except:
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)

    return decorated


@user_blueprint.route('/')
def index():
    return "User route"


@user_blueprint.route('/signup', methods=['POST'])
def signup():
    """
    Send sign up form or create a new User

    Parameters: none

    Returns:
        form(json) or redirect(/home)
    """

    user = User.signup(
        first_name=request.form['firstName'],
        last_name=request.form['lastName'],
        username=request.form['username'],
        email=request.form['email'],
        password=request.form['password']
    )

    db.session.commit()

    print(user.id)
    Pantry.createPantry(user.id)

    db.session.commit()

    return redirect('http://localhost:8080/login')


@user_blueprint.route('/login', methods=['POST'])
def login():
    req_json = request.get_json()
    username = req_json['username']
    password = req_json['password']

    user = User.authenticate(username, password)
    if user:
        user = user.to_dict()
        token = jwt.encode({'user': user, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(hours=24)}, jwt_key)
        return jsonify({'token': token})

    else:
        return redirect('http://localhost:8080/users/login')


@user_blueprint.route('/home', methods=['GET'])
def home():
    token = request.headers.get('Authorization')

    token = token.split(' ')
    token = token[1]

    if not token:
        return jsonify({'message': 'Token is missing'})

    try:
        data = jwt.decode(token, jwt_key, algorithms="HS256")
        return jsonify(data['user'])
    except:
        return jsonify({'message': 'token is invalid'})
