from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskserver.config import Config
from flask_cors import CORS  # Import thư viện CORS



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class= Config):
    app = Flask(__name__)
    CORS(app) # active CORS
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskserver.users.routes import users
    from flaskserver.main.routes import main
    from flaskserver.chat.routes import chat

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(chat)    

    return app
