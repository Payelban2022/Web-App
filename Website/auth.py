from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Log in<p>"

@auth.route("/logout")
def logout():
    return "<p>Log out<p>"

@auth.route("/sign_up")
def sign_up():
    return "<p>Sign up<p>"
