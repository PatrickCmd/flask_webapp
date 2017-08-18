from flask import Flask, render_template, redirect, url_for, request, \
    session, flash, g
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import os

# creating the application object
app = Flask(__name__)

# config
# app.config.from_object('config.DevelopmentConfig')
app.config.from_object(os.environ['APP_SETTINGS'])

# creating sqlalchemy object
db = SQLAlchemy(app)

from models import *


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized to access to this page, Please login", "danger")
            return redirect(url_for('login'))
    return wrap

# use a route decorator to link function to a url
@app.route('/')
@login_required
def index():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid login credentials, please try again!'
        else:
            session['logged_in'] = True
            flash("You are logged in", "success")
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You are logged out", "warning")
    return redirect(url_for('login'))


# start the server with run function
if __name__ == '__main__':
    app.run()
