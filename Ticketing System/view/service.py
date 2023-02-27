from flask import render_template

def index_logic():
    return render_template("index.html", page="Base")

def login_logic(status):
    return render_template("login_page.html", page="Login", status=status)

def register_logic(status):
    return render_template("register_page.html", page="Register", status=status)