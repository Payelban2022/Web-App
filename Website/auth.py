from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='ERROR')
        elif len(firstName) or len(lastName) < 2:
            flash('Name must be greater than 1 characters.', category='ERROR')

        elif password1 != password2:
            flash('Passwords does not match.', category='ERROR')
        elif len(password1) < 8:
            flash(' Password must be at least 8 characters.', category='ERROR')
        else:

            flash('Account created!', category='SUCCESS')



    return render_template("sign_up.html")
