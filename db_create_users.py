from app import db
from models import User

# insert data
db.session.add(User("patrick", "patrick@gmail.com", "arsenal2016"))
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("cmdtelnet", "telnet@cmd.com", "cmd123"))

# commit the changes
db.session.commit()
