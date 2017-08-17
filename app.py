from flask import Flask, render_template, redirect, url_for, request, \
    session, flash, g
from functools import wraps
import sqlite3

# creating the application object
app = Flask(__name__)

app.secret_key = '@#$%&*?@$#cmd123telnet$#%@$@'
app.database = 'sample.db'

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
    posts = []
    try:
        g.db = connect_db()
        cur = g.db.execute('SELECT * FROM posts')
        # print(cur.fetchall())
        posts = [dict(title = row[0], description = row[1]) \
                 for row in cur.fetchall()]
        print(posts)
        g.db.close()
    except sqlite3.OperationalError:
        flash("There is no database to connect to", "warning")
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

def connect_db():
    return sqlite3.connect(app.database)

# start the server with run function
if __name__ == '__main__':
    app.run(debug=True)
