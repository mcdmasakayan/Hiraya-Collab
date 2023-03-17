from flask import request, jsonify
from model.user.data import User

def show_all_users():
    data = request.get_json()

    if 'password' in data and data['password'] == 'admin':
        users = User.query.filter_by(archived=False).all()
        users_list = []
        columns = ['_id', 'username', 'password', 'first_name', 'last_name']

        for user in users:
            data = {}
            
            for column in columns:
                data[column] = user._id

            users_list.append(data)
        
        return jsonify({'users':users_list})
    
    return jsonify({'message':'Invalid Password.'})