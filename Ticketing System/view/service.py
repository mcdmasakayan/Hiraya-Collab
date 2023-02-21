from flask import render_template

def index_logic():
    return render_template("index.html", page="Index")

def login_logic():
    status = "Login Successful!"
    print("SYSTEM: Account found in database.")

    return render_template("login_page.html", page="Login", status=status)

def register_logic():
    status = "Registration Successful!"
    print("SYSTEM: Account inserted in database.")

    return render_template("register_page.html", page="Register", status=status)