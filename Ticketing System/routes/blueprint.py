from flask import Blueprint
from controller.control import admin
from controller.control import index, login, register
from controller.control import logout, create_project, open_project, create_task, open_task, move_task
from controller.control import create_subtask, open_subtask, move_subtask

blueprint = Blueprint('blueprint', __name__)

#Admin
blueprint.route('/hirayamnl', methods=['POST'])(admin)

#Login System
blueprint.route('/', methods=['GET'])(index)
blueprint.route('/login', methods=['POST'])(login)
blueprint.route('/register', methods=['POST'])(register)

#Home Page
blueprint.route('/logout', methods=['POST'])(logout)
blueprint.route('/create-project', methods=['GET'])(create_project)
blueprint.route('/open-project', methods=['GET'])(open_project)
blueprint.route('/create-task', methods=['GET'])(create_task)
blueprint.route('/open-task', methods=['GET'])(open_task)
blueprint.route('/move-task', methods=['GET'])(move_task)
blueprint.route('/create-subtask', methods=['GET'])(create_subtask)
blueprint.route('/open-subtask', methods=['GET'])(open_subtask)
blueprint.route('/move-subtask', methods=['GET'])(move_subtask)