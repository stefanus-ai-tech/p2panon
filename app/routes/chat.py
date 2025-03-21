from flask import Blueprint, request, jsonify
from datetime import datetime
import humanize
from app.models.chat import Room, Message
from app.database import db
import uuid

chat_bp = Blueprint('chat', __name__, url_prefix='/api/chat')

def format_timestamp(timestamp):
    """Format a timestamp into a more precise format"""
    try:
        if isinstance(timestamp, str):
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        elif isinstance(timestamp, datetime):
            dt = timestamp
        else:
            return "Unknown time"
            
        # Format as exact time instead of relative time
        return dt.strftime("%I:%M %p, %d %b") # Example: "03:45 PM, 25 Aug"
        
    except Exception as e:
        print(f"Error formatting timestamp: {e}")
        return "Unknown time"

@chat_bp.route('/rooms', methods=['POST'])
def create_room():
    """Create a new chat room"""
    try:
        room_id = str(uuid.uuid4())
        new_room = Room(room_id=room_id)
        
        db.session.add(new_room)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Chat room created successfully',
            'data': {
                'id': new_room.id,
                'room_id': new_room.room_id,
                'created_at': new_room.created_at.isoformat()
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': f'Failed to create room: {str(e)}',
            'data': None
        }), 500

@chat_bp.route('/rooms/<string:room_id>', methods=['GET'])
def get_room(room_id):
    """Get a chat room by ID"""
    try:
        room = Room.query.filter_by(room_id=room_id).first()
        
        if not room:
            return jsonify({
                'status': 'error',
                'message': 'Room not found',
                'data': None
            }), 404
        
        return jsonify({
            'status': 'success',
            'message': 'Chat room retrieved successfully',
            'data': {
                'id': room.id,
                'room_id': room.room_id,
                'created_at': room.created_at.isoformat()
            }
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to retrieve room: {str(e)}',
            'data': None
        }), 500

@chat_bp.route('/rooms/<string:room_id>/messages', methods=['GET'])
def get_room_messages(room_id):
    """Get all messages for a room"""
    try:
        messages = Message.query.filter_by(room_id=room_id).order_by(Message.timestamp).all()
        
        formatted_messages = []
        for message in messages:
            formatted_message = {
                'id': message.id,
                'room_id': message.room_id,
                'sender_id': message.sender_id,
                'content': message.content,
                'timestamp': message.timestamp.isoformat(),
                'formattedTime': format_timestamp(message.timestamp)
            }
            formatted_messages.append(formatted_message)
        
        return jsonify({
            'status': 'success',
            'message': 'Messages retrieved successfully',
            'data': formatted_messages
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to retrieve messages: {str(e)}',
            'data': None
        }), 500

@chat_bp.route('/rooms/<string:room_id>/messages', methods=['POST'])
def create_message(room_id):
    """Create a new message in a room"""
    try:
        data = request.json
        if not data or 'sender_id' not in data or 'content' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Missing required fields',
                'data': None
            }), 400
        
        room = Room.query.filter_by(room_id=room_id).first()
        if not room:
            return jsonify({
                'status': 'error',
                'message': 'Room not found',
                'data': None
            }), 404
        
        new_message = Message(
            room_id=room_id,
            sender_id=data['sender_id'],
            content=data['content']
        )
        
        db.session.add(new_message)
        db.session.commit()
        
        # Format the message with the timestamp before sending to frontend
        message_data = {
            'id': new_message.id,
            'room_id': new_message.room_id,
            'sender_id': new_message.sender_id,
            'content': new_message.content,
            'timestamp': new_message.timestamp.isoformat(),
            'formattedTime': format_timestamp(new_message.timestamp)
        }
        
        return jsonify({
            'status': 'success',
            'message': 'Message sent successfully',
            'data': message_data
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': f'Failed to send message: {str(e)}',
            'data': None
        }), 500
