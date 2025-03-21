from app.database import db
from datetime import datetime

class Room(db.Model):
    __tablename__ = 'rooms'
    
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.String(36), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    messages = db.relationship('Message', backref='room', lazy=True)
    
    def __repr__(self):
        return f'<Room {self.room_id}>'

class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.String(36), db.ForeignKey('rooms.room_id'), nullable=False)
    sender_id = db.Column(db.String(36), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Message {self.id} in Room {self.room_id}>'
