from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users, Robots, Algorithms, Results

class RegistrationForm(FlaskForm):
     first_name = StringField('First Name',
        validators = [
            DataRequired()
        ]
     )
     last_name = StringField('Last Name',
        validators = [
            DataRequired()
        ]
     )

     email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
     )
     password = PasswordField('Password',
        validators = [
            DataRequired()
        ]
     )
     confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
     )
     submit = SubmitField('Sign Up!')

     def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RobotForm(FlaskForm):
    model_name = StringField('Model Name',
        validators= [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )

    drive_type = StringField('Drive Type',
        validators=[
            DataRequired(),
            Length(min=2,max=50)
        ]
    )
    
    height = IntegerField('Height(mm)')
    width = IntegerField('Width(mm)')
    length = IntegerField('Length(mm)')

    submit = SubmitField('Add!')

class UpdateRobotForm(FlaskForm):
    model_name = StringField('Model Name',
        validators= [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )

    drive_type = StringField('Drive Type',
        validators=[
            DataRequired(),
            Length(min=2,max=50)
        ]
    )

    height = IntegerField('Height(mm)')
    width = IntegerField('Width(mm)')
    length = IntegerField('Length(mm)')

    submit = SubmitField('Update!')

class AlgorithmForm(FlaskForm):
    algorithm_name = StringField('Algorithm name',
        validators = [
            DataRequired(),
            Length(min=2,max=50)
        ]
    )
    
    movement_type = StringField('Movement Type',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    submit = SubmitField('Add!')

class UpdateAlgorithmForm(FlaskForm):
    algorithm_name = StringField('Algorithm name',
        validators = [
            DataRequired(),
            Length(min=2,max=50)
        ]
    )
    movement_type = StringField('Movement Type',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    submit = SubmitField('Update!')

class ResultForm(FlaskForm):
    robot_id = SelectField(coerce=int)
    algorithm_id = SelectField(coerce=int)
    time_taken = IntegerField('Time taken(s)',
        validators=[
            DataRequired()
        ]
    )   
    submit = SubmitField('Add!')
    def __init__(self):
        super(ResultForm, self).__init__()
        self.robot_id.choices = [(g.id, g.model_name) for g in Robots.query.all()]
        self.algorithm_id.choices = [(g.id, g.algorithm_name) for g in Algorithms.query.all()]      
