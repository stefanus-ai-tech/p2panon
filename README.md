# P2P Anonymous Chat

A simple, anonymous peer-to-peer chat application with a Flask backend and Streamlit frontend.

## Features

- Create private chat rooms
- Join existing chat rooms with room ID
- Anonymous messaging with no registration required
- Real-time chat updates
- Clean, minimalist UI

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (optional but recommended)

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

#### Method 2: Using Docker Compose

```bash
docker-compose up -d
```

### Accessing the Application

- Backend API: http://localhost:5000/api
- Frontend: http://localhost:8501

## Usage

1. Open the frontend URL in your web browser
2. Create a new chat room or join an existing one with a room ID
3. Share the room ID with people you want to chat with
4. Start chatting anonymously!

## License

MIT
