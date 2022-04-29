import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xyz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ##### Flask-Mail configurations #####
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'infooveriq@gmail.com'
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    # MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql+psycopg2://postgres:19862814@localhost/data'


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
                              'postgresql+psycopg2://postgres:19862814@localhost/data'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
                              'postgresql+psycopg2://postgres:19862814@localhost/data'