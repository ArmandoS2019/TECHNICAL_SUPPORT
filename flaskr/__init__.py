from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskr.login.login import login_blueprint
from flaskr.main.main import main_blueprint
from flaskr.config import Config

#------------------------------
import pymysql
pymysql.install_as_MySQLdb()
#PYMYSQL IS FOR DEVELOPMENT----

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.register_blueprint(login_blueprint)
app.register_blueprint(main_blueprint)
