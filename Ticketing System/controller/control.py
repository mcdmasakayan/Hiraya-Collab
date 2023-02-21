from view.service import login_logic, register_logic, index_logic

def index():
    return index_logic()

def login():
    return login_logic()

def register():
    return register_logic()