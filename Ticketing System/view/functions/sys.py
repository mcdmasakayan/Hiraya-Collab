import hashlib
from flask import jsonify
from model.machine import User as users

def hash_string(str):
    hash_str = hashlib.md5(str.encode()).hexdigest()

    return hash_str

def get_users():
    data = {}
    for x in users.query.all():
        data.update({x._id:{
                    'email': x.email,
                    'username': x.username,
                    'password': x.password,
                    'firstname': x.first_name,
                    'lastname': x.last_name,
                    'verified': x.verified,
                    'archived': x.archived
                }})
        
    return jsonify(data)