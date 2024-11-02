from models.schemas.userSchema import user_schema, users_schema
from services import userService
from flask import jsonify, request
from marshmallow import ValidationError


def save():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    user_save = userService.save(user_data)
    if user_save is not None:
        return user_schema.jsonify(user_save), 201
    else:
        return jsonify({"message": "Failed to save."}), 400

def find_all():
    users = userService.find_all()
    return users_schema.jsonify(users), 200

def login():
    info = request.json
    user = userService.login_user(info['username'], info['password'])
    if user:
        return jsonify(user), 200
        

    else:
        resp = {
            'status': 'error',
            'message': 'user does not exist'
        }
        return jsonify(resp), 404