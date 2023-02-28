from flask import Blueprint
from controller.control import index, login, register
from controller.control import create_project, open_project, logout

blueprint = Blueprint('blueprint', __name__)

#Login System
blueprint.route('/', methods=['GET'])(index)
blueprint.route('/login', methods=['POST', 'GET'])(login)
blueprint.route('/register', methods=['POST', 'GET'])(register)

#Home Page
blueprint.route('/create-project', methods=['GET'])(create_project)
blueprint.route('/open-project', methods=['GET'])(open_project)
blueprint.route('/logout', methods=['GET'])(logout)