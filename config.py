import os
import dotenv
dotenv.load_dotenv('keys.env')
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TMP_KEY'
    # DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'tmp.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
