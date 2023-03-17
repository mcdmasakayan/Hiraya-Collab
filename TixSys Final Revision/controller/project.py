from flask import request
from controller.task import create_task, move_task, archive_task
from model.project.crud import create_project, open_project, archive_project

def project_system(**kwargs):
    user_request = request.get_json()

    if 'command' in user_request:
        if user_request['command'] == 'create_project' and request.method == 'POST':
            response = create_project()

            return response
        
        elif user_request['command'] == 'open_project' and request.method == 'GET':
            response = open_project(kwargs)

            return response
        
        elif user_request['command'] == 'archive_project' and request.method == 'PATCH':
            response = archive_project(kwargs)

            return response
        
        elif user_request['command'] == 'create_task' and request.method == 'POST':
            response = create_task(kwargs)

            return response
        
        elif user_request['command'] == 'archive_task' and request.method == 'PATCH':
            response = archive_task(kwargs)

            return response
        
        elif user_request['command'] == 'move_task' and request.method == 'PATCH':
            response = move_task(kwargs)

            return response