from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ChatRoom(Base):
    __tablename__ = 'chat_rooms'
    
    id = Column(Integer, primary_key=True)
    room_id = Column(String(64), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    messages = relationship('Message', backref='chat_room', lazy='dynamic')
    
    def __repr__(self):
        return f'<ChatRoom {self.room_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'room_id': self.room_id,
            'created_at': self.created_at.isoformat()
        }

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)
    chat_room_id = Column(Integer, ForeignKey('chat_rooms.id'), nullable=False)
    sender_id = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Message {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'chat_room_id': self.chat_room_id,
            'sender_id': self.sender_id,
            'content': self.content,
            'timestamp': self.timestamp.isoformat()
        }
