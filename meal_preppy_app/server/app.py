# server/app.py
import os
from typing import List

# Flask imports
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

# Database imports
from sqlalchemy import SQLAlchemy
from models import List, Pantry, User

# Routes imports
from routes.user_blueprint import user_blueprint
from routes.api_blueprint import api_blueprint

# Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///meal_preppy'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

# Database setup
db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.
    """

    db.app = app
    db.init_app(app)


connect_db(app)

# Routes
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(api_blueprint, url_prefix="/api")

CORS(app)


# @app.route('/courses', methods=['GET', 'POST'])
# def all_courses():
#     response_object = {'status': 'success'}
#     if request.method == 'POST':
#         post_data = request.get_json()
#         COURSES.append({
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'paperback': post_data.get('paperback')
#         })
#         response_object['message'] = 'Course added!'
#     else:
#         response_object['courses'] = COURSES
#     return jsonify(response_object)
