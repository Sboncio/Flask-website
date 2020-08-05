from application import db
from application.models import Robots, Algorithms, Users, Results 

db.drop_all()
db.create_all()
