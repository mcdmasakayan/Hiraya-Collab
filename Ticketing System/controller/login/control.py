from flask import request, session
from view.login.service import index_logic, login_logic, register_logic

def index():
    return index_logic()

def login():
    return login_logic()

def register():
    return register_logic()