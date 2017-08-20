from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, session  # pragma: no cover
from flask_login import login_user, login_required, logout_user  # pragma: no cover
from functools import wraps  # pragma: no cover

from .forms import LoginForm, RegisterForm  # pragma: no cover
from project import db  # pragma: no cover
from project.models import User, bcrypt  # pragma: no cover


################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)   # pragma: no cover


###### Helper function #######
# login required decorator
# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash("Unauthorized to access to this page, Please login", "danger")
#             return redirect(url_for('home.welcome'))
#     return wrap  # pragma: no cover

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            # print(user.name, user.password)
            if user is not None and \
                bcrypt.check_password_hash(user.password, request.form['password']):
                # session['logged_in'] = True
                login_user(user)
                flash("You are logged in", "success")
                return redirect(url_for('home.index'))
            else:
                error = 'Invalid login credentials, please try again!'
    return render_template('login.html', form=form, error=error)

@users_blueprint.route('/logout')
@login_required
def logout():
    # session.pop('logged_in', None)
    logout_user()
    flash("You are logged out", "warning")
    return redirect(url_for('home.welcome'))

@users_blueprint.route(
    '/register/', methods=['GET', 'POST'])   # pragma: no cover
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.index'))
    return render_template('register.html', form=form)

