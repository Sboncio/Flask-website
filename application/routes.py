from flask import render_template, redirect, url_for
from application import app, db
from application.models import Robots, Algorithms
from application.forms import RobotForm, AlgorithmForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/robots')
def robot():
    robotData = Robots.query.all()
    return render_template('robot.html',title='Robot',robots=robotData)

@app.route('/algorithms')
def algorithm():
    algorithmData = Algorithms.query.all()
    return render_template('algorithm.html',title='Algorithm',algorithms=algorithmData)

@app.route('/add_algorithm', methods=['GET','POST'])
def addAlgorithm():
    form = AlgorithmForm()
    if form.validate_on_submit():
        algorithmData = Algorithms(
            algorithm_name = form.algorithm_name.data,
            movement_type = form.movement_type.data
        )
        
        db.session.add(algorithmData)
        db.session.commit()

        return redirect(url_for('algorithm'))
    else:
        print(form.errors)
    return render_template('add_algorithm.html', title='Add Algorithm', form=form)
    

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
