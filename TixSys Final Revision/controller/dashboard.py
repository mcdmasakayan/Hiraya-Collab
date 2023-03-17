from flask import request
from controller.login import logout_user
from controller.project import create_project, archive_project
from model.dashboard.crud import open_dashboard

def dashboard_system():
    user_request = request.get_json()

    if 'command' in user_request:
        if user_request['command'] == 'open_dashboard' and request.method == 'GET':
            response = open_dashboard()

            return response
        
        elif user_request['command'] == 'create_project' and request.method == 'POST':
            response = create_project()

            return response
        
        elif user_request['command'] == 'archive_project' and request.method == 'PATCH':
            response = archive_project()

            return response
        
        elif user_request['command'] == 'logout_user' and request.method == 'PATCH':
            response = logout_user()

            return response
        
        