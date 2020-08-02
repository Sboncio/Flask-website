from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    userresult = db.relationship('Results',backref='author',lazy=True)    

    def __repr__(self):
        return ''.join(['UserID: ',str(self.id),'\r\n','Email: ', self.email])


class Robots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(50),nullable=False, unique=True)
    drive_type = db.Column(db.String(50))
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    length = db.Column(db.Integer)
    robotresult = db.relationship('Results',backref='robot', lazy=True)

    def __repr__(self):
        return ''.join([
            'Robot id: ', self.id,' Model_name: ', self.model_name, '\r\n',
            'Drive type: ', self.drive_type])

class Algorithms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    algorithm_name = db.Column(db.String(50), nullable=False, unique=True)
    movement_type = db.Column(db.String(50))
    algorithmresult = db.relationship('Results',backref='algorithm', lazy=True)    

    def __repr__(self):
        return ''.join([
            'Algorithm name: ', self.algorithm_name, '\r\n',
            'Movement type: ', self.movement_type])

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey('robots.id'), nullable=False)
    algorithm_id = db.Column(db.Integer, db.ForeignKey('algorithms.id'), nullable=False)
    time_taken = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
