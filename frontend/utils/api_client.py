import requests
import json

class ApiClient:
    """Client for interacting with the backend API"""
    
    def __init__(self, base_url):
        self.base_url = base_url
        
    def create_room(self):
        """Create a new chat room"""
        response = requests.post(f"{self.base_url}/chat/rooms")
        if response.status_code == 201:
            return response.json()['data']
        else:
            error_msg = response.json().get('message', 'Unknown error')
            raise Exception(f"Failed to create room: {error_msg}")
            
    def get_room(self, room_id):
        """Get information about a chat room"""
        response = requests.get(f"{self.base_url}/chat/rooms/{room_id}")
        if response.status_code == 200:
            return response.json()['data']
        elif response.status_code == 404:
            return None
        else:
            error_msg = response.json().get('message', 'Unknown error')
            raise Exception(f"Failed to get room: {error_msg}")
            
    def send_message(self, room_id, sender_id, content):
        """Send a message to a chat room"""
        data = {
            "sender_id": sender_id,
            "content": content
        }
        response = requests.post(
            f"{self.base_url}/chat/rooms/{room_id}/messages",
            json=data
        )
        if response.status_code == 201:
            return response.json()['data']
        else:
            error_msg = response.json().get('message', 'Unknown error')
            raise Exception(f"Failed to send message: {error_msg}")
            
    def get_messages(self, room_id):
        """Get all messages from a chat room"""
        response = requests.get(f"{self.base_url}/chat/rooms/{room_id}/messages")
        if response.status_code == 200:
            return response.json()['data']
        else:
            error_msg = response.json().get('message', 'Unknown error')
            raise Exception(f"Failed to get messages: {error_msg}")
