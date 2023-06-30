from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


DataRequired_ru = 'Поле обязательно для заполнения'
Email_ru = 'Некорректный Email'
EqualTo_ru = 'Пароли не совпадают'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message=DataRequired_ru)])
    password = PasswordField('Password', validators=[DataRequired(message=DataRequired_ru)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Войти')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message=DataRequired_ru)])
    email = StringField('Email', validators=[DataRequired(message=DataRequired_ru), Email(message=Email_ru)])
    password = PasswordField('Password', validators=[DataRequired(message=DataRequired_ru), Length(min=8)])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(message=DataRequired_ru), EqualTo('password', message=EqualTo_ru)])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Это имя пользователя уже занято')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Эта почта уже используется')