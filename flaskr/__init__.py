from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskr.config import Config
# from flaskr.models.models import db
#------------------------------
import pymysql
pymysql.install_as_MySQLdb()
#PYMYSQL IS FOR DEVELOPMENT----
# db = SQLAlchemy()

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)
db.init_app(app)

from flaskr.login.login import login_blueprint
from flaskr.main.main import main_blueprint
from flaskr.admin.admin import admin_blueprint

app.register_blueprint(login_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(admin_blueprint)
