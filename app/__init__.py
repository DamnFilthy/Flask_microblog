"""
В Python подкаталог, содержащий файл __init__.py, считается пакетом и может быть импортирован.
Когда вы импортируете пакет, __init__.py выполняет и определяет,
какие символы предоставляют пакет для внешнего мира.
"""
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask_bootstrap import Bootstrap
from flask_moment import Moment

# Инициализируем приложение
application = Flask(__name__)
application.config.from_object(Config)
# Создаем экземпляр почты
mail = Mail(application)
# Создаем экземпляр логина
login = LoginManager(application)
login.login_view = 'login'
# Подключаем базу данных
db = SQLAlchemy(application)
migrate = Migrate(application, db)
# Подключаем bootstrap
bootstrap = Bootstrap(application)
# Настраиваем дату и время
moment = Moment(application)

if not application.debug:
    if application.config['MAIL_SERVER']:
        auth = None
        if application.config['MAIL_USERNAME'] or application.config['MAIL_PASSWORD']:
            auth = (application.config['MAIL_USERNAME'], application.config['MAIL_PASSWORD'])
        secure = None
        if application.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(application.config['MAIL_SERVER'], application.config['MAIL_PORT']),
            fromaddr='no-reply@' + application.config['MAIL_SERVER'],
            toaddrs=application.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        application.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    application.logger.addHandler(file_handler)

    application.logger.setLevel(logging.INFO)
    application.logger.info('Microblog startup')

"""
модуль routes импортируется внизу, а не наверху скрипта,
как это всегда делается. Нижний импорт является обходным путем
для циклического импорта, что является общей проблемой
при использовании приложений Flask.
модуль routes должен импортировать переменную приложения,
определенную в этом скрипте, поэтому, поместив один из
взаимных импортов внизу, вы избежите ошибки, которая возникает
из взаимных ссылок между этими двумя файлами.
Модуль - models определит структуру базы данных.
"""
from app import routes, models, errors
