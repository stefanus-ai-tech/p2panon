#!/bin/bash

echo "Installing dependencies for P2P Anonymous Chat..."

# Make sure pip is up to date
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

echo "Installation complete. You should now be able to run the application."
