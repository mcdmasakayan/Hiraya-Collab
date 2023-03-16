from flask import Blueprint
from model.variables import Link
from controller.admin import show_user_list
from controller.user import login_system, signup_system
from controller.project import new_project, open_project, remove_project
from controller.task import new_task, open_task, remove_task
from controller.subtask import new_subtask, remove_subtask
from controller.dashboard import dashboard, remove_user

bp = Blueprint('bp', __name__)

#Admin
bp.route(Link.admin, methods=['GET'])(show_user_list)

#Settings System
bp.route(Link.settings, methods=['PATCH'])(remove_user)

#Login System
bp.route(Link.login, methods=['POST'])(login_system)
bp.route(Link.register, methods=['POST'])(signup_system)

#Dashboard System
bp.route(Link.dashboard, methods=['GET'])(dashboard)
bp.route(Link.dashboard, methods=['POST'])(new_project)
bp.route(Link.dashboard, methods=['PATCH'])(remove_project)

#Project System
bp.route(Link.project, methods=['GET'])(open_project)
bp.route(Link.project, methods=['POST'])(new_task)
bp.route(Link.project, methods=['PATCH'])(remove_project)
bp.route(Link.task, methods=['PATCH'])(remove_task)

#Task System
bp.route(Link.task, methods=['GET'])(open_task)
bp.route(Link.task, methods=['POST'])(new_subtask)
bp.route(Link.task, methods=['PATCH'])(remove_task)

#Subtask System
bp.route(Link.task, methods=['PATCH'])(remove_subtask)