from flask import Blueprint
from model.variables import Link
from controller.admin import admin_system
from controller.login import login_system
from controller.project import project_system
from controller.task import task_system
from controller.dashboard import dashboard_system
from controller.settings import settings_system

bp = Blueprint('bp', __name__)

bp.route(Link.admin, methods=['POST'])(admin_system)
bp.route(Link.settings, methods=['GET', 'PATCH'])(settings_system)
bp.route(Link.login, methods=['POST'])(login_system)
bp.route(Link.dashboard, methods=['GET', 'POST', 'PATCH'])(dashboard_system)
bp.route(Link.project, methods=['GET', 'POST', 'PATCH'])(project_system)
bp.route(Link.task, methods=['GET', 'POST', 'PATCH'])(task_system)