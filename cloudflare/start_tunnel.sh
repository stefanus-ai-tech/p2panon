#!/bin/bash

# Make sure this script is executable (chmod +x start_tunnel.sh)

# Check if cloudflared is installed
if ! command -v cloudflared &> /dev/null; then
    echo "cloudflared is not installed. Please install it first."
    echo "Visit https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation"
    exit 1
fi

# Directory containing this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
CONFIG_PATH="$SCRIPT_DIR/config.yml"

echo "Starting Cloudflare Tunnel for P2P Anonymous Chat backend..."
echo "Using config: $CONFIG_PATH"

# Run the tunnel
cloudflared tunnel --config "$CONFIG_PATH" run
