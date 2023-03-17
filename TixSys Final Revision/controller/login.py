from flask import request
from model.user.crud import verify_user, register_user, logout_user

def login_system():
    user_request = request.get_json()
    
    if 'command' in user_request and request.method == 'POST':
        if user_request['command'] == 'login':
            response = verify_user()

            return response
        
        elif user_request['command'] == 'register':
            response = register_user()

            return response