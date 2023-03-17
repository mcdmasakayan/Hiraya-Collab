from flask import request
from model.settings.crud import archive_user

def settings_system(**kwargs):
    user_request = request.get_json()

    if 'command' in user_request:
        if user_request['command'] == 'archive_user' and request.method == 'PATCH':
            response = archive_user(kwargs)

            return response