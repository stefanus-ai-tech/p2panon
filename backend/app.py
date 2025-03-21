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
    
    @app.route('/')
    def index():
        """Return a simple HTML page indicating the tunnel is running"""
        hostname = os.environ.get('TUNNEL_HOSTNAME', 'chat.stefanusadri.my.id')
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>P2P Anonymous Chat - Backend</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                    background-color: #f5f5f5;
                }}
                .container {{
                    background-color: white;
                    border-radius: 10px;
                    padding: 20px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    max-width: 600px;
                    margin: 0 auto;
                }}
                .status {{
                    color: #4CAF50;
                    font-weight: bold;
                }}
                .info {{
                    margin-top: 20px;
                    font-size: 14px;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>P2P Anonymous Chat</h1>
                <p>Backend API Status: <span class="status">RUNNING</span></p>
                <p>Cloudflare Tunnel: <span class="status">ACTIVE</span></p>
                <p>Hostname: <strong>{hostname}</strong></p>
                
                <div class="info">
                    <p>API Endpoints:</p>
                    <ul style="text-align: left; display: inline-block;">
                        <li>Health Check: <code>/health</code></li>
                        <li>API Base: <code>/api</code></li>
                    </ul>
                </div>
                
                <div class="info">
                    <p>To use the web interface, open: <a href="http://localhost:8501">http://localhost:8501</a></p>
                </div>
            </div>
        </body>
        </html>
        """
        return html

    @app.route('/health')
    def health():
        return {'status': 'healthy'}
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
