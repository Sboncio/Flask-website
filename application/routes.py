from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Robots, Algorithms, Users
from application.forms import RobotForm, AlgorithmForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user,logout_user, login_required

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
@login_required
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
@login_required
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(
            email=form.email.data, 
            password=hash_pw,
            first_name = form.first_name.data,
            last_name = form.last_name.data)
    
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.password.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
