from flask import Blueprint
from controller.control import index, login, register

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/login', methods=['POST', 'GET'])(login)
blueprint.route('/register', methods=['POST', 'GET'])(register)