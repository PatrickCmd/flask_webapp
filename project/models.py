from project import db  # pragma: no cover
from project import bcrypt  # pragma: no cover

from sqlalchemy import ForeignKey  # pragma: no cover
from sqlalchemy.orm import relationship  # pragma: no cover


class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)  # pragma: no cover
    title = db.Column(db.String, nullable=False)  # pragma: no cover
    description = db.Column(db.String, nullable=False)  # pragma: no cover
    author_id = db.Column(db.Integer, ForeignKey('users.id'))  # pragma: no cover

    def __init__(self, title, description, author_id):
        self.title = title
        self.description = description
        self.author_id = author_id

    def __repr__(self):
        return '<title {}>'.format(self.title)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        print(self.password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)
