from flask_login import LoginManager, UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User_tbl(UserMixin, db.Model):
    __tablename__ = 'User_tbl'
    id = db.Column(db.Integer, primary_key=True)
    my_relation_medicenter = db.relationship('Personalinfo_tbl')
    cedula_id = db.Column(db.String(11), unique=True)
    num_carnet_id_pass = db.Column(db.String(11), unique=True)
    #---------------------------------------------------------------
    firstname  = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    birthday = db.Column(db.DateTime)
    rank = db.Column(db.String(7))
    email_address  = db.Column(db.String(70), unique=True)
    celphone = db.Column(db.String(10))
    direccion_workplace_police  = db.Column(db.String(50))
    work_unit  = db.Column(db.String(50))
    nivel_admin  = db.Column(db.String(10))
    created_user_account = db.Column(db.DateTime, default=datetime.now())

class Personalinfo_tbl(UserMixin, db.Model):
    
    __tablename__ = 'Personalinfo_tbl'
    id = db.Column(db.Integer, primary_key=True)
    my_user_id = db.Column(db.Integer, db.ForeignKey('User_tbl.id'))
    
    provincia_location = db.Column(db.String(70))
    address_home_location = db.Column(db.String(70))
    status_of_home = db.Column(db.String(20))
    documents_pdf = db.Column(db.Text)
    images_home1 = db.Column(db.Text)
    images_home2 = db.Column(db.Text)
    
    created_personal_info = db.Column(db.DateTime, default=datetime.now())
    
    
