from model.admin.crud import get_all_users

def show_user_list():
    response = get_all_users()

    return response