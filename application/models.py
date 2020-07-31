from application import db

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
