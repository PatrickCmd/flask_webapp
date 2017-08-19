from flask import Flask, render_template, redirect, url_for, request, \
    session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from functools import wraps
import os

# creating the application object
# config
# app.config.from_object('config.DevelopmentConfig')
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# creating sqlalchemy object
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# register blue print
app.register_blueprint(users_blueprint)


###### Helper function #######
# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized to access to this page, Please login", "danger")
            return redirect(url_for('users.login'))
    return wrap


# use a route decorator to link function to a url
@app.route('/')
@login_required
def index():
    try:
        posts = db.session.query(BlogPost).all()
    except:
        flash("No database connection", "warning")
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# start the server with run function
if __name__ == '__main__':
    app.run()
