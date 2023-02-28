from view.login.service import index_logic, login_logic, register_logic
from view.home.service import pcreate_logic, popen_logic

#Base
def index():
    return index_logic()

#Login System
def login():
    return login_logic()

def register():
    return register_logic()

#Home Page
def create_project():
    return pcreate_logic()

def open_project():
    return popen_logic()