import os


class Config:
    SECRET_KEY = 'cc14319c74eba1b498b97ab01b5ef3f3'  # Za bezbednosni celi
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # ///-a relative path to a current file(modulewe are cur in
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
