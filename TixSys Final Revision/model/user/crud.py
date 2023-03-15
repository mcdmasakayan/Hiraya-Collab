from flask import request, jsonify
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from model.init_db import db
from model.user.data import User
from middleware.session import add_to_session

def verify_user():
    entry = ''
    users = User.query.filter_by(archived=False).all()
    data = request.get_json()

    if (('username' in data) and ('password' in data)):
        entry = 'username'
        
    elif (('email' in data) and ('password' in data)):
        entry = 'email'
    
    if entry:
        for user in users:
                if ((data[entry] == getattr(user, entry)) and
                    (check_password_hash(user.password, data['password']))):
                       
                    add_to_session(user.public_id)

                    return jsonify({'message':'Access Granted.'})

    return jsonify({'message':'Access Denied.'})

def register_user():
    users = User.query.filter_by(archived=False).all()
    data = request.get_json()

    for user in users:
        if data['email'] == user.email:
            return jsonify({'message':'Email already exists. User not registered.'})
        elif data['username'] == user.username:
            return jsonify({'message':'Username already exists. User not registered.'})

    hashed_password = generate_password_hash(data['password'], method='sha256')

    user = User(public_id=str(uuid4()),
                email=data['email'],
                username=data['username'],
                password=hashed_password,
                first_name=data['first_name'],
                last_name=data['last_name'],
                verified=False,
                archived=False)
    
    db.session.add(user)
    db.session.commit()

    return jsonify({'message':'User registered.'})