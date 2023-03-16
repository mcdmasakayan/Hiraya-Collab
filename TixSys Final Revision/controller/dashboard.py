from model.dashboard.crud import get_dashboard_data
from model.dashboard.settings.crud import archive_user

def dashboard():
    response = get_dashboard_data()

    return response

def remove_user():
    response = archive_user()

    return response