from flask import Blueprint
from controllers.userController import find_all, login, save

user_blueprint = Blueprint('user_bp', __name__)

user_blueprint.route('/', methods=['POST'])(save)
user_blueprint.route('/', methods=['GET'])(find_all)
user_blueprint.route('/login', methods=['POST'])(login)