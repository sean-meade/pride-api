from .extensions import db 

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(50), unique=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(350), unique=True)    
