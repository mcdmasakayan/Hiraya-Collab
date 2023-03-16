from flask import Blueprint
from controller.admin import show_user_list
from controller.user import login_system, signup_system
from controller.project import new_project, open_project
from controller.task import new_task, open_task
from controller.subtask import new_subtask
from controller.dashboard import dashboard

bp = Blueprint('bp', __name__)

#Admin
bp.route('/admin', methods=['GET'])(show_user_list)

#Login System
bp.route('/login', methods=['POST'])(login_system)
bp.route('/register', methods=['POST'])(signup_system)

#Dashboard System
bp.route('/dashboard', methods=['GET'])(dashboard)
bp.route('/dashboard', methods=['POST'])(new_project)

#Project System
bp.route('/dashboard/<string:project_name>', methods=['GET'])(open_project)
bp.route('/dashboard/<string:project_name>', methods=['POST'])(new_task)

#Task System
bp.route('/dashboard/<string:project_name>/<string:task_name>', methods=['GET'])(open_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>', methods=['POST'])(new_subtask)