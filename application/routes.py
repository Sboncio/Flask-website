from flask import render_template, redirect, url_for
from application import app, db
from application.models import Robots
from application.forms import RobotForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/robots')
def robot():
    robotData = Robots.query.all()
    return render_template('robot.html',title='Robot',robots=robotData)

@app.route('/add_robot', methods=['GET','POST'])
def addRobot():
    form = RobotForm()
    if form.validate_on_submit():
        robotData = Robots(
            model_name = form.model_name.data,
            drive_type = form.drive_type.data,
            height = form.height.data,
            width = form.width.data,
            length = form.length.data
        )

        db.session.add(robotData)
        db.session.commit()

        return redirect(url_for('robot'))

    else:
        print(form.errors)

    return render_template('add_robot.html', title='Add Robot', form=form)
