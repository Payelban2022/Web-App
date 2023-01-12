from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods =['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route("/logout")
def logout():
    return "<p>Log out<p>"

@auth.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")
