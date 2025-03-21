import uuid
from flask import Blueprint, request, jsonify
from ..services.chat_service import create_chat_room, get_chat_room, add_message, get_messages
from ..utils.helpers import generate_response

bp = Blueprint('chat', __name__, url_prefix='/api/chat')

@bp.route('/rooms', methods=['POST'])
def create_room():
    try:
        room_id = str(uuid.uuid4())
        room = create_chat_room(room_id)
        return generate_response(room.to_dict(), 'Chat room created successfully', 201)
    except Exception as e:
        return generate_response(None, str(e), 500)

@bp.route('/rooms/<room_id>', methods=['GET'])
def get_room(room_id):
    try:
        room = get_chat_room(room_id)
        if not room:
            return generate_response(None, 'Room not found', 404)
        return generate_response(room.to_dict(), 'Chat room retrieved successfully', 200)
    except Exception as e:
        return generate_response(None, str(e), 500)

@bp.route('/rooms/<room_id>/messages', methods=['POST'])
def post_message(room_id):
    try:
        data = request.get_json()
        sender_id = data.get('sender_id')
        content = data.get('content')
        
        if not sender_id or not content:
            return generate_response(None, 'Sender ID and content are required', 400)
            
        message = add_message(room_id, sender_id, content)
        return generate_response(message.to_dict(), 'Message sent successfully', 201)
    except Exception as e:
        return generate_response(None, str(e), 500)

@bp.route('/rooms/<room_id>/messages', methods=['GET'])
def get_room_messages(room_id):
    try:
        messages = get_messages(room_id)
        return generate_response([msg.to_dict() for msg in messages], 'Messages retrieved successfully', 200)
    except Exception as e:
        return generate_response(None, str(e), 500)
