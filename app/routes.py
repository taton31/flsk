from app import app, db
from flask import render_template, flash, redirect, url_for, request, jsonify
from werkzeug.urls import url_parse
from app.forms import LoginForm, SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.rate import get_rate


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page:
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return render_template('succes_signup.html', title='Succes')
    return render_template('signup.html', form=form)


@app.route('/converter')
def converter():
    return render_template('converter.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('users.html', users = users)


@app.route('/convert', methods=['POST'])
def convert():
    res = get_rate(request.form['cur_from'],
                    request.form['cur_to'],
                    float(request.form['value']))
    return jsonify({'text': round(res, 2)})