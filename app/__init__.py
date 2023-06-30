# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # # from flask_migrate import Migrate

# # def create_app():
# #     app = Flask(__name__)

# #     app.config.from_pyfile('../config.py')

# #     return app

# # app = create_app()
# # # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/sqlite_DB.db"
# # # db.init_app(app)
# # db = SQLAlchemy(app)


# # # migrate = Migrate(app, db)

# from flask import Flask
# from flask_migrate import Migrate, MigrateCommand
# # from flask_mail import Mail, Message
# from flask_sqlalchemy import SQLAlchemy
# # from flask_script import Manager, Command, Shell
# from flask_login import LoginManager
# import os, config

# # создание экземпляра приложения
# app = Flask(__name__)
# # app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
# app.config.from_object('config.DevelopementConfig')

# # инициализирует расширения
# db = SQLAlchemy(app)
# # mail = Mail(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

# # import views
# from . import views
# # from . import forum_views
# # from . import admin_views

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models