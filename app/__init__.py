from flask import Flask
from flask_cors import CORS
from app.database import db
from app.routes.chat import chat_bp
import os

def create_app():
    app = Flask(__name__)
    
    # Configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///chat.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(chat_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
