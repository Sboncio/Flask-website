from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ',str(self.id),'\r\n','Email: ', self.email])


class Robots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(50),nullable=False, unique=True)
    drive_type = db.Column(db.String(50))
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    length = db.Column(db.Integer)

    def __repr__(self):
        return ''.join([
            'Robot id: ', self.id,' Model_name: ', self.model_name, '\r\n',
            'Drive type: ', self.drive_type])

class Algorithms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    algorithm_name = db.Column(db.String(50), nullable=False, unique=True)
    movement_type = db.Column(db.String(50))

    def __repr__(self):
        return ''.join([
            'Algorithm name: ', self.algorithm_name, '\r\n',
            'Movement type: ', self.movement_type])

