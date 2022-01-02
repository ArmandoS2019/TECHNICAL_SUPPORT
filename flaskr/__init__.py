from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskr.config import Config
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import imghdr
import os
#------------------------------
import pymysql
pymysql.install_as_MySQLdb()
#PYMYSQL IS FOR DEVELOPMENT----

app = Flask(__name__)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login.login"
login_manager.login_message = "Necesitas iniciar sesión."
login_manager.login_message_category = "danger"

login_manager.refresh_view = "login.login"
login_manager.needs_refresh_message =(u"Nececita autenticarse nuevamente")
login_manager.needs_refresh_message_category = "info"

app.config.from_object(Config)
csrf = CSRFProtect(app)
db.init_app(app)
login_manager.init_app(app)

from flaskr.login.login import login_blueprint
from flaskr.main.main import main_blueprint
from flaskr.admin.admin import admin_blueprint

app.register_blueprint(login_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(admin_blueprint)
