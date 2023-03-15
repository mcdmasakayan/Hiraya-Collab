from model.user.crud import verify_user, register_user

def login_system():
    response = verify_user()

    return response

def signup_system():
    response = register_user()

    return response