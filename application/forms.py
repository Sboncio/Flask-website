from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users

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
