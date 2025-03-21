from flask import Flask
from flask_cors import CORS

# Fix imports to work when run directly
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Use absolute imports if running as main script
if __name__ == '__main__':
    from backend.config import Config
    from backend.routes import chat_routes
    from backend.services.db_service import init_db
else:
    # Use relative imports when imported as a module
    from .config import Config
    from .routes import chat_routes 
    from .services.db_service import init_db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # Initialize database
    init_db()
    
    # Register blueprints
    app.register_blueprint(chat_routes.bp)
    
    @app.route('/health')
    def health():
        return {'status': 'healthy'}
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
