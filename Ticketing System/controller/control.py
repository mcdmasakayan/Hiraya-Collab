from view.login.service import admin_logic
from view.login.service import index_logic, login_logic, register_logic
from view.home.service import pcreate_logic, popen_logic, logout_logic
from view.home.service import tcreate_logic, topen_logic, tmove_logic, smove_logic
from view.home.service import screate_logic, sopen_logic

#Admin
def admin():
    return admin_logic()

#Base
def index():
    return index_logic()

#Login System
def login():
    return login_logic()

def register():
    return register_logic()

#Home Page
def logout():
    return logout_logic()

def create_project():
    return pcreate_logic()

def open_project():
    return popen_logic()

def create_task():
    return tcreate_logic()

def open_task():
    return topen_logic()

def move_task():
    return tmove_logic()

def create_subtask():
    return screate_logic()

def open_subtask():
    return sopen_logic()

def move_subtask():
    return smove_logic()