import requests
import jwt
from flask import Blueprint, jsonify, request
from config import api_key, jwt_key
from models.User import User

base_url = "https://api.spoonacular.com/recipes/"

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/')
def index():
    return "Api route"


@api_blueprint.route('/recipes')
def getRecipies():
    """Gets top 10 recipes

    Returns:
        json: a json object of the 10 recipies
    """

    token = request.headers.get('Authorization')
    token = token.split(' ')
    token = token[1]

    if not token:
        return jsonify({'message': 'Token is missing'})

    data = jwt.decode(token, jwt_key, algorithms="HS256")
    user = User.query.get(data['user']['id'])
    ingredients = user.pantry[0].ingredients

    # Loops through ingredients and makes their properties into dicts
    ingredient_list = map(
        lambda ingredient: ingredient.to_dict(), ingredients)
    ingredient_list = list(ingredient_list)

    ingredient_slug = []
    for ingredient in ingredient_list:
        ingredient_slug.append(ingredient["ingredient_name"])

    # ingredient_slug[len(ingredient_slug)-1
    #                 ] = ingredient_slug[len(ingredient_slug)-1].split(',')[0]

    print(',+'.join(ingredient_slug))

    # Things I need for card: title, image, id, summary, instructions{steps [{number, step, equipment{id, name}, ingredients{id, name}, length{number, unit}}]}, extended_ingredients {id, name}
    r = requests.get(
        f'{base_url}findByIngredients?ingredients={ingredient_slug}&number=6&apiKey={api_key}')
    return jsonify(r.json())
