from flask import request
from view.service import login_logic, register_logic
from model.machine import login_user, register_user

def index():
    return "None"

def login():
    status = "Start Logging In."
    if request.method == "POST":
        username = request.form['username-entry']
        password = request.form['password-entry']
        status = login_user(username, password)

    return login_logic(status)

def register():
    status = "Start Registration."
    if request.method == "POST":
        email = request.form['email-entry-r']
        username = request.form['username-entry-r']
        password = request.form['password-entry-r']
        first_name = request.form['fname-entry-r']
        last_name = request.form['lname-entry-r']
        status = register_user(email, username, password, first_name, last_name, False, False)

    return register_logic(status)