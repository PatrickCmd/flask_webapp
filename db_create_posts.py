from app import db
from models import BlogPost

# create database and db tables
db.create_all()

# insert
db.session.add(BlogPost("FLASK", "MICRO PYTHON FRAMEWORK", 1))
db.session.add(BlogPost("PYTHON", "HIGH LEVEL PROGRAMMING LANGUAGE", 1))
db.session.add(BlogPost("DJANGO", "BATTERY PYTHON FRAMEWORK", 2))
db.session.add(BlogPost("POSTGRESQL", "CREATED AN INSTANCE OF POSTGRESQL", 3))
db.session.add(BlogPost("ANDELA", "FELLOWSHIP FOUNDATION", 2))
db.session.add(BlogPost("PATRICK", "BEST PYTHON PROGRAMMER EVER", 3))

# commit
db.session.commit()
