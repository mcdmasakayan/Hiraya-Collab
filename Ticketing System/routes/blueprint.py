from flask import Blueprint
from controller.control import index, login, register, create_project, open_project

blueprint = Blueprint('blueprint', __name__)

#Login System
blueprint.route('/', methods=['GET'])(index)
blueprint.route('/login', methods=['POST', 'GET'])(login)
blueprint.route('/register', methods=['POST', 'GET'])(register)

#Home Page
blueprint.route('/create-project', methods=['GET'])(create_project)
blueprint.route('/open-project', methods=['GET'])(open_project)