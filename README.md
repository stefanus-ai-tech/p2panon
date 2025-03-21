# P2P Anonymous Chat

A simple, anonymous peer-to-peer chat application with a Flask backend and Streamlit frontend.

## Features

- Create private chat rooms
- Join existing chat rooms with room ID
- Anonymous messaging with no registration required
- Real-time chat updates
- Clean, minimalist UI
- **Secure tunneling via Cloudflare Tunnel**

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (optional but recommended)
- Cloudflared CLI (for tunneling the backend API)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/p2panon.git
cd p2panon
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
```

Edit the `.env` file with your configuration settings.

5. Install Cloudflared:

Follow the instructions at https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation to install Cloudflared on your system.

### Running the Application

#### Method 1: Using Python directly

1. Start the backend server:

```bash
cd backend
python app.py
```

2. In a new terminal, start the frontend:

```bash
cd frontend
streamlit run app.py
```

3. Start the Cloudflare Tunnel:

```bash
chmod +x cloudflare/start_tunnel.sh
./cloudflare/start_tunnel.sh
```

#### Method 2: Using Docker Compose

```bash
docker-compose up -d
```

### Setting up Cloudflare Tunnel

1. Log in to Cloudflared once before running the tunnel:

```bash
mkdir -p cloudflare/.cloudflared
cloudflared tunnel login
```

2. Create a new tunnel:

```bash
cloudflared tunnel create p2panon-backend
```

3. Copy the credentials JSON file to the cloudflare/.cloudflared directory

4. Update the hostname in cloudflare/config.yml to your desired hostname

5. Create a DNS record for your tunnel:

```bash
cloudflared tunnel route dns p2panon-backend your-tunnel-hostname.example.com
```

### Accessing the Application

- Backend API (local): http://localhost:5000/api
- Backend API (tunneled): https://your-tunnel-hostname.example.com/api
- Frontend: http://localhost:8501

## Usage

1. Open the frontend URL in your web browser
2. Create a new chat room or join an existing one with a room ID
3. Share the room ID with people you want to chat with
4. Start chatting anonymously!

## License

MIT
