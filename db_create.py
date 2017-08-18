from app import db
from models import BlogPost

# create database and db tables
db.create_all()

# insert
db.session.add(BlogPost("FLASK", "MICRO PYTHON FRAMEWORK"))
db.session.add(BlogPost("PYTHON", "HIGH LEVEL PROGRAMMING LANGUAGE"))
db.session.add(BlogPost("DJANGO", "BATTERY PYTHON FRAMEWORK"))
db.session.add(BlogPost("POSTGRESQL", "CREATED AN INSTANCE OF POSTGRESQL"))
db.session.add(BlogPost("ANDELA", "FELLOWSHIP FOUNDATION"))
db.session.add(BlogPost("PATRICK", "BEST PYTHON PROGRAMMER EVER"))

# commit
db.session.commit()
