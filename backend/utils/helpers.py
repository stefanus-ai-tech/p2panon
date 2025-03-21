from flask import jsonify
import uuid

def generate_response(data, message, status_code):
    """Generate a standardized API response"""
    response = {
        'data': data,
        'message': message,
        'status': 'success' if status_code < 400 else 'error'
    }
    return jsonify(response), status_code

def generate_unique_id():
    """Generate a unique identifier"""
    return str(uuid.uuid4())
