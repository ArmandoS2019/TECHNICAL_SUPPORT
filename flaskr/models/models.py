from flask_login import UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flaskr import db
# db = SQLAlchemy()
class User_tbl(UserMixin, db.Model):
    __tablename__ = 'User_tbl'
    id = db.Column(db.Integer, primary_key=True)
    my_relation_personalinf = db.relationship('Technicalsupport_tbl')
    
    cedula_id = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(200), unique=True)
    #---------------------------------------------------------------
    firstname  = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    birthday = db.Column(db.DateTime)
    rank = db.Column(db.String(7))
    email_address  = db.Column(db.String(70), unique=True)
    cellphone = db.Column(db.String(10))
    direccion_workplace_police  = db.Column(db.String(50))
    work_unit  = db.Column(db.String(50))
    nivel_admin  = db.Column(db.String(10))
    created_user_account = db.Column(db.DateTime, default=datetime.now())

class Technicalsupport_tbl(UserMixin, db.Model):
    
    __tablename__ = 'Technicalsupport_tbl'
    id = db.Column(db.Integer, primary_key=True)
    my_user_id = db.Column(db.Integer, db.ForeignKey('User_tbl.id'))
    
    firstname_lastname = db.Column(db.String(70))
    direction_support = db.Column(db.String(70))
    work_unit_support = db.Column(db.String(70))
    phone_support = db.Column(db.String(70))
    type_of_support = db.Column(db.String(70))
    
    comment_support = db.Column(db.String(200))
    image_support1 = db.Column(db.Text)
    image_support2 = db.Column(db.Text)
    
    created_technical_support = db.Column(db.DateTime, default=datetime.now())
    
    
