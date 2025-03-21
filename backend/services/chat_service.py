from ..models.chat import ChatRoom, Message
from .db_service import get_db_session

def create_chat_room(room_id):
    """Create a new chat room"""
    session = get_db_session()
    chat_room = ChatRoom(room_id=room_id)
    session.add(chat_room)
    session.commit()
    return chat_room

def get_chat_room(room_id):
    """Get a chat room by its ID"""
    session = get_db_session()
    return session.query(ChatRoom).filter(ChatRoom.room_id == room_id).first()

def add_message(room_id, sender_id, content):
    """Add a new message to a chat room"""
    session = get_db_session()
    chat_room = get_chat_room(room_id)
    
    if not chat_room:
        raise Exception("Chat room not found")
        
    message = Message(chat_room_id=chat_room.id, sender_id=sender_id, content=content)
    session.add(message)
    session.commit()
    return message

def get_messages(room_id):
    """Get all messages for a chat room"""
    session = get_db_session()
    chat_room = get_chat_room(room_id)
    
    if not chat_room:
        raise Exception("Chat room not found")
        
    return session.query(Message).filter(Message.chat_room_id == chat_room.id).all()
