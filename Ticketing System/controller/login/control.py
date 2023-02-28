from flask import request
from view.login.service import index_logic, login_logic, register_logic

def index():
    return index_logic()

def login():
    if request.method == "POST":
        username = request.form['username-entry']
        password = request.form['password-entry']
        login_logic(username, password)

def register():
    if request.method == "POST":
        email = request.form['email-entry-r']
        username = request.form['username-entry-r']
        password = request.form['password-entry-r']
        first_name = request.form['fname-entry-r']
        last_name = request.form['lname-entry-r']
        register_logic(email, username, password, first_name, last_name)