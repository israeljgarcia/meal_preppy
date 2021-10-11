from flask import Blueprint, jsonify, request, redirect, session
from models.PantryIngredient import PantryIngredient
from models.Pantry import Pantry
from models.User import User
from models.Shared import db
from config import jwt_key
import jwt
pantry_blueprint = Blueprint('pantry', __name__)


@pantry_blueprint.route('/')
def getPantryIngredients():
    """Gets the ingredients in the user's pantry in json format

    Returns:
        ingredient_list[json]: the list of ingredients in json
    """

    ingredient_list = {}

    token = request.headers.get('Authorization')

    token = token.split(' ')
    token = token[1]

    if not token:
        return jsonify({'message': 'Token is missing'})

    try:
        data = jwt.decode(token, jwt_key, algorithms="HS256")
        user = User.query.get(data['user']['id'])
        ingredients = user.pantry[0].ingredients

        # Loops through ingredients and makes their properties into dicts
        ingredient_list = map(
            lambda ingredient: ingredient.to_dict(), ingredients)
        ingredient_list = list(ingredient_list)
    except:
        return jsonify({'message': 'token is invalid'})

    return jsonify(ingredient_list)


@pantry_blueprint.route('/addingredient', methods=["POST"])
def add_ingredient():
    """adds new ingredient to the user's pantry
    """

    # TODO Remove hard code to get pantry id from session
    # TODO! Add data sanitizing for form data
    token = request.headers.get('Authorization')

    token = token.split(' ')
    token = token[1]

    if not token:
        return jsonify({'message': 'Token is missing'})

    try:
        data = jwt.decode(token, jwt_key, algorithms="HS256")
        user = User.query.get(data['user']['id'])

        req_json = request.get_json()
        ingredient_name = req_json['ingredientName']
        quantity = req_json['quantity']
        unit = req_json['unit']

        pantry = user.pantry[0]
        PantryIngredient.create_ingredient(
            pantry.id, ingredient_name, quantity, unit)

        db.session.commit()

        return jsonify({'messsage': 'Successfully added ingredient!'})
    except:
        return jsonify({'message': 'error'})
