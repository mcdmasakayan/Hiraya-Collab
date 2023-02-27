from flask import render_template, jsonify
from model.database.machine import User as users

def index_logic():
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

def login_logic(status):
    return render_template("login_page.html", page="Login", status=status)

def register_logic(status):
    return render_template("register_page.html", page="Register", status=status)