from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
bootstrap = Bootstrap(app)
login.login_view = 'login'
login.login_message = "Для просмотра этой страницы необходимо авторизоваться"

# def get_locale():
#     return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel = Babel(app, locale_selector=get_locale)
# # babel.init_app(app, locale_selector=get_locale)

from app import routes, models, log