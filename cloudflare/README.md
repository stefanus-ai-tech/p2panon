# Setting up Cloudflare Tunnel for P2P Anonymous Chat

This guide will help you set up a Cloudflare Tunnel to securely expose your backend API to the internet.

## Prerequisites

1. A Cloudflare account
2. Cloudflared CLI installed on your system
3. A domain name managed by Cloudflare

## Step-by-Step Setup

### 1. Install Cloudflared

Follow the instructions at [Cloudflare's official documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation) to install Cloudflared for your operating system.

### 2. Authenticate Cloudflared

```bash
cloudflared tunnel login
```

This will open a browser window to authenticate with your Cloudflare account. After authentication, it will generate a cert.pem file typically in ~/.cloudflared/.

### 3. Create a Tunnel

```bash
cloudflared tunnel create p2panon-backend
```

This command creates a new tunnel named "p2panon-backend" and generates a credentials file (JSON) that you'll need for establishing the connection.

### 4. Copy Credentials File

Copy the generated credentials JSON file to the `.cloudflared` directory within this project:

```bash
mkdir -p .cloudflared
cp ~/.cloudflared/*.json .cloudflared/credentials.json
```

### 5. Configure the Tunnel

Edit the `config.yml` file in this directory:

```yaml
# Cloudflared tunnel configuration
tunnel: p2panon-backend # The name you provided when creating the tunnel
credentials-file: /path/to/credentials.json # Update this path

ingress:
  - hostname: your-tunnel-hostname.example.com # Update this to your desired hostname
    service: http://localhost:5000
  - service: http_status:404
```

### 6. Create a DNS Record

Create a DNS record that points your hostname to the tunnel:

```bash
cloudflared tunnel route dns p2panon-backend your-tunnel-hostname.example.com
```

### 7. Start the Tunnel

Run the provided script:

```bash
./start_tunnel.sh
```

Or run the cloudflared command directly:

```bash
cloudflared tunnel --config config.yml run
```

### 8. Update Frontend Configuration

Make sure your frontend is configured to use the tunneled API URL:

1. Update your `.env` file with:

   ```
   API_URL=https://your-tunnel-hostname.example.com/api
   ```

2. Or update the Streamlit secrets.toml with:
   ```
   API_URL = "https://your-tunnel-hostname.example.com/api"
   ```

## Troubleshooting

- **Connection Issues**: Make sure port 5000 is accessible locally
- **Authentication Issues**: Re-run `cloudflared tunnel login`
- **DNS Issues**: Ensure your DNS records are properly set up in the Cloudflare dashboard
