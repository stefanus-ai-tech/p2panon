#!/usr/bin/env python3
"""
Entry point script for running the backend server.
Run this from the project root directory.
"""
from backend.app import create_app
from backend.services.db_service import init_db

if __name__ == '__main__':
    # Initialize the database
    init_db()
    
    # Create and run the app
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
