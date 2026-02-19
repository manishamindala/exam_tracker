from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User, Exam, Alarm
from datetime import datetime

main = Blueprint('main', __name__)

# --- AUTHENTICATION ---
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid email or password!', 'danger')
    return render_template('login.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if User.query.filter_by(email=email).first():
            flash('Email already exists!', 'danger')
            return redirect(url_for('main.signup'))
        new_user = User(email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('signup.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

# --- DASHBOARD / WORKSPACE ---
@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        new_exam = Exam(
            subject=request.form.get('subject'),
            date=request.form.get('date'),
            notes=request.form.get('notes'),
            user_id=current_user.id
        )
        db.session.add(new_exam)
        db.session.commit()
        return redirect(url_for('main.dashboard'))

    user_exams = Exam.query.filter_by(user_id=current_user.id).all()
    exams_list = []
    today = datetime.now().date()
    for e in user_exams:
        try:
            e_date = datetime.strptime(e.date, '%Y-%m-%d').date()
            days_left = (e_date - today).days
        except:
            days_left = "N/A"
        exams_list.append({'data': e, 'days_left': days_left})
    return render_template('dashboard.html', exams=exams_list)

# --- CALENDAR GRID ---
@main.route('/calendar')
@login_required
def calendar_page():
    user_exams = Exam.query.filter_by(user_id=current_user.id).all()
    return render_template('calendar.html', exams=user_exams)

# --- ALARMS ---
@main.route('/alarms', methods=['GET', 'POST'])
@login_required
def alarms_page():
    if request.method == 'POST':
        new_alarm = Alarm(
            label=request.form.get('label'), 
            time=request.form.get('time'), 
            user_id=current_user.id
        )
        db.session.add(new_alarm)
        db.session.commit()
        return redirect(url_for('main.alarms_page'))
    user_alarms = Alarm.query.filter_by(user_id=current_user.id).all()
    return render_template('alarms.html', alarms=user_alarms)

# --- DELETE ACTIONS ---
@main.route('/delete-exam/<int:id>')
@login_required
def delete_exam(id):
    exam = Exam.query.get_or_404(id)
    if exam.user_id == current_user.id:
        db.session.delete(exam)
        db.session.commit()
    return redirect(url_for('main.dashboard'))

@main.route('/delete-alarm/<int:id>')
@login_required
def delete_alarm(id):
    alarm = Alarm.query.get_or_404(id)
    if alarm.user_id == current_user.id:
        db.session.delete(alarm)
        db.session.commit()
    return redirect(url_for('main.alarms_page'))