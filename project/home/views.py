from flask import flash, url_for, render_template, redirect, session, \
    Blueprint, request  # pragma: no cover
from flask_login import login_required, current_user  # pragma: no cover
from functools import wraps  # pragma: no cover

from project import app, db  # pragma: no cover
from project.models import BlogPost  # pragma: no cover
from .forms import MessageForm  # pragma: no cover


################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
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
#             return redirect(url_for('users.login'))
#     return wrap  # pragma: no cover


# use a route decorator to link function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.', 'success')
        return redirect(url_for('home.index'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template(
            'index.html', posts=posts, form=form, error=error)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')
