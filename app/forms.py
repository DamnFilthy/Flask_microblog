"""
Расширение Flask-WTF использует классы Python для представления веб-форм.
Класс формы просто определяет поля формы как переменные класса.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('NickName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')


def validate_email(email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
        raise ValidationError('Please use a different email address.')


def validate_username(username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
        raise ValidationError('Please use a different username.')


# Форма редактирования профиля
class EditProfileForm(FlaskForm):
    username = StringField('Имя: ', validators=[DataRequired()])
    about_me = TextAreaField('Обо мне: ', validators=[Length(min=0, max=140)])
    submit = SubmitField('Подтвердить')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


# Форма для редактирования статьи
class EditPostForm(FlaskForm):
    title_post = TextAreaField('Заголовок', validators=[DataRequired(), Length(min=10, max=60)])
    body_post = TextAreaField('Текст', validators=[DataRequired(), Length(min=10, max=2900)])
    save = SubmitField('Сохранить изменения')


# Форма для загрузки аватара
class ChangeAvatarForm(FlaskForm):
    photo = StringField('Введите URL-link', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')


# Пустая форма для подтверждения действия
class EmptyForm(FlaskForm):
    submit = SubmitField('Подтвердить')


# Пустая форма для удаления
class PostFormDelete(FlaskForm):
    delete = SubmitField('Удалить')


# Форма нового сообщения
class PostForm(FlaskForm):
    title = TextAreaField("Заголовок", validators=[DataRequired(), Length(min=10, max=60)])

    post = TextAreaField('Текст', validators=[DataRequired(), Length(min=10, max=2900)])
    submit = SubmitField('Отправить')


# Форма для сброса пароля
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Сбросить')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[
        DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Submit')
