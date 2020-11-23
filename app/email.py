from flask_mail import Message
from app import mail, application
from flask import render_template
from threading import Thread


# Асинхронная функция
def send_async_email(application, msg):
    with application.application_context():
        mail.send(msg)


# функция отправки почты
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(application, msg)).start()


# Электронное письмо для сброса пароля
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[MetalSnake] Reset Your Password',
               sender=application.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
