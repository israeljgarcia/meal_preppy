from flask import Blueprint
from config import api_key

base_url = "https://api.spoonacular.com/recipes/"

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/')
def index():
    return 'API'
