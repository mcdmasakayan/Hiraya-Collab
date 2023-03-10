from flask import Blueprint
from controller.control import index
from controller.control import show_login_system, show_registration_system
from controller.control import show_dashboard, logout_account
from controller.control import create_project, open_project, show_project, delete_project 
from controller.control import create_task, open_task, show_task, move_task, delete_task
from controller.control import create_subtask, complete_subtask, delete_subtask

bp = Blueprint('main_bp', __name__)

#Login System
bp.route('/', methods=['GET', 'POST'])(index)
bp.route('/login', methods=['GET', 'POST'])(show_login_system)
bp.route('/register', methods=['GET', 'POST'])(show_registration_system)

#Dashboard
bp.route('/dashboard', methods=['GET', 'POST'])(show_dashboard)
bp.route('/dashboard/logout', methods=['GET', 'POST'])(logout_account)
bp.route('/dashboard/create-project', methods=['GET', 'POST'])(create_project)
bp.route('/dashboard/open-project', methods=['GET', 'POST'])(open_project)
bp.route('/dashboard/<project_name>', methods=['GET', 'POST'])(show_project)
bp.route('/dashboard/delete-project', methods=['GET', 'POST'])(delete_project)
bp.route('/dashboard/<project_name>/create-task', methods=['GET', 'POST'])(create_task)
bp.route('/dashboard/<project_name>/open-task', methods=['GET', 'POST'])(open_task)
bp.route('/dashboard/<project_name>/move-task', methods=['GET', 'POST'])(move_task)
bp.route('/dashboard/<project_name>/delete-task', methods=['GET', 'POST'])(delete_task)
bp.route('/dashboard/<project_name>/<task_name>', methods=['GET', 'POST'])(show_task)
bp.route('/dashboard/<project_name>/<task_name>/create-subtask', methods=['GET', 'POST'])(create_subtask)
bp.route('/dashboard/<project_name>/<task_name>/complete-subtask', methods=['GET', 'POST'])(complete_subtask)
bp.route('/dashboard/<project_name>/<task_name>/delete-subtask', methods=['GET', 'POST'])(delete_subtask)