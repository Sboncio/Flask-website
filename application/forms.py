from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

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
