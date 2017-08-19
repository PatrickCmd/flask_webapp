from flask import flash, url_for, render_template, redirect, session, \
    Blueprint
from functools import wraps

from project import app, db
from project.models import BlogPost


################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
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
            return redirect(url_for('users.login'))
    return wrap


# use a route decorator to link function to a url
@home_blueprint.route('/')
@login_required
def index():
    try:
        posts = db.session.query(BlogPost).all()
    except:
        flash("No database connection", "warning")
    return render_template('index.html', posts=posts)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')
