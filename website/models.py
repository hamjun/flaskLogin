from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

#singular
class User(db.Model, UserMixin):
    #id is automaticlly done
    id = db.Column(db.Integer, primary_key=True)
    #need max length defined when we declare a string
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #one to many relationship 
    #user in is 'id' in User 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    