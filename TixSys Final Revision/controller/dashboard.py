from model.dashboard.crud import get_dashboard_data

def dashboard():
    response = get_dashboard_data()

    return response