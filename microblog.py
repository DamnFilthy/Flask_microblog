"""
Чтобы завершить приложение, вам нужно создать сценарий Python
на верхнем уровне, определяющий экземпляр приложения Flask.
Давайте назовем этот скрипт microblog.py и определим его как
одну строку, которая импортирует экземпляр приложения
"""

from app import application, db
from app.models import User, Post, Notification, Message


# функция создает контекакщьст оболочки, который добавляет
# экземпляр и модели базы данных в сеанс оболочки
@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification}
