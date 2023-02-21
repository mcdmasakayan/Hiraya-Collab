from flask import render_template

def index_logic():
    return render_template("index.html", page="Index")

def login_logic():
    return render_template("login_page.html", page="Login")

def register_logic():
    return render_template("register_page.html", page="Register")