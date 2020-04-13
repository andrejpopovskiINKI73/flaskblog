from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
admin = Admin()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail()


# this is so the that the extension object doesn't get bound to the application!, this is stored on the extension
# object, so that one extension object can be used for multiple apps we initialize the extensions at the top of our
# file, but without the app variable (we remove the app variable within all the functions above!)
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(posts)
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

    # from flaskblog import routes   we need to import these here because when we run the application it can find them
    #  also, we do the import here to not get errors of the type Circular Imports!!!
