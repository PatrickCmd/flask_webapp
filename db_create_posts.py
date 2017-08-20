from project import app, db
from project.models import BlogPost

# create database and db tables
db.create_all()

# insert
db.session.add(BlogPost("FLASK", "MICRO PYTHON FRAMEWORK", 7))
db.session.add(BlogPost("PYTHON", "HIGH LEVEL PROGRAMMING LANGUAGE", 7))
db.session.add(BlogPost("DJANGO", "BATTERY PYTHON FRAMEWORK", 8))
db.session.add(BlogPost("POSTGRESQL", "CREATED AN INSTANCE OF POSTGRESQL", 9))
db.session.add(BlogPost("ANDELA", "FELLOWSHIP FOUNDATION", 8))
db.session.add(BlogPost("PATRICK", "BEST PYTHON PROGRAMMER EVER", 9))

# commit
db.session.commit()
