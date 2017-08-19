from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, session  # pragma: no cover
from app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from functools import wraps


################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)   # pragma: no cover


###### Helper function #######
# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized to access to this page, Please login", "danger")
            return redirect(url_for('welcome'))
    return wrap

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid login credentials, please try again!'
        else:
            session['logged_in'] = True
            flash("You are logged in", "success")
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@users_blueprint.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You are logged out", "warning")
    return redirect(url_for('welcome'))
