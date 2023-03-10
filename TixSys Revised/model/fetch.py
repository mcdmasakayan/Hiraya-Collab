import hashlib
from flask import request

error_response = '<h1>Error 404 Page.</h1>'

def get_credentials():
    try:
        email = request.args.get('email')
        username = request.args.get('username')
        password = hashlib.md5(request.args.get('password').encode()).hexdigest()

        credentials = {'email':email,
                    'username':username,
                    'password':password}
        
    except (UnboundLocalError, AttributeError):
        return error_response
    
    return credentials

def get_user_info():
    try:
        email = request.args.get('email')
        username = request.args.get('username')
        password = hashlib.md5(request.args.get('password').encode()).hexdigest()
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        
        user_info = {'email':email,
                    'username':username,
                    'password':password,
                    'first_name':first_name,
                    'last_name':last_name}
        
    except (UnboundLocalError, AttributeError):
        return error_response
    
    return user_info

def get_project_info():
    try:
        name = request.args.get('name')
        description = request.args.get('description')

        project_info = {'name':name,
                        'description':description}
        
    except (UnboundLocalError, AttributeError):
        return error_response
    
    return project_info

def get_task_info():
    try:
        name = request.args.get('name')
        description = request.args.get('description')

        task_info = {'name':name,
                     'description':description}
        
    except (UnboundLocalError, AttributeError):
        return error_response
    
    return task_info

def get_subtask_info():
    try:
        name = request.args.get('name')
        description = request.args.get('description')

        subtask_info = {'name':name,
                     'description':description}
        
    except (UnboundLocalError, AttributeError):
        return error_response
    
    return subtask_info

def get_transfer_info():
    try:
        name = request.args.get('name')
        progress = request.args.get('progress')

        transfer_info = {'name':name,
                         'progress':progress}
        
    except (UnboundLocalError, AttributeError):
        return error_response
    
    return transfer_info