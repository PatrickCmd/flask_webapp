from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

# creating the application object
# config
# app.config.from_object('config.DevelopmentConfig')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(os.environ['APP_SETTINGS'])
# creating sqlalchemy object
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

# register blue print
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
