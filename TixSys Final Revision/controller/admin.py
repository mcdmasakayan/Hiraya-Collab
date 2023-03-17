from flask import request
from model.admin.crud import show_all_users

def admin_system():
    user_request = request.get_json()

    if 'command' in user_request:
        if user_request['command'] == 'show_all_users' and request.method == 'POST':
            response = show_all_users()

        return response