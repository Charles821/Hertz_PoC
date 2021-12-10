import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
SECRET_KEY = 'supersecretkey'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

DEBUG = True

MAIL_SERVER = "smtp1.hertz.com"
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
