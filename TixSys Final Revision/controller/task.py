from flask import request
from controller.subtask import new_subtask, remove_subtask
from model.task.crud import create_task, open_task, archive_task, move_task

def task_system(**kwargs):
    user_request = request.get_json()

    if 'command' in user_request:
        if user_request['command'] == 'create_task' and request.method == 'POST':
            response = create_task(kwargs)

            return response
        
        elif user_request['command'] == 'open_task' and request.method == 'GET':
            response = open_task(kwargs)

            return response

        elif user_request['command'] == 'archive_task' and request.method == 'PATCH':
            response = archive_task(kwargs)

            return response
        
        elif user_request['command'] == 'transfer_task' and request.method == 'PATCH':
            response = move_task(kwargs)

            return response
        
        elif user_request['command'] == 'create_subtask' and request.method == 'POST':
            response = new_subtask(kwargs)

            return response
        
        elif user_request['command'] == 'archive_subtask' and request.method == 'PATCH':
            response = remove_subtask(kwargs)

            return response
        