import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Класс для хранения переменных конфигурации
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.bd')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.mail.ru'
    MAIL_PORT = '587'
    MAIL_USE_TLS = '1'
    MAIL_USERNAME = 'metalsnake@inbox.ru'
    MAIL_PASSWORD = 'ASB@#1993678'
    ADMINS = ['metalsnake@inbox.ru']

    POSTS_PER_PAGE = 3
