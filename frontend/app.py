import streamlit as st
import uuid
import os
from components.sidebar import render_sidebar
from components.chat_interface import render_chat_interface
from utils.api_client import ApiClient

def main():
    # Initialize session state
    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())
    
    if 'api_client' not in st.session_state:
        # Try to get API URL from secrets, environment variables, or use default
        try:
            api_base_url = st.secrets.get("API_URL")
        except FileNotFoundError:
            # Fall back to environment variables or default
            api_base_url = os.environ.get("API_URL", "http://localhost:5000/api")
            st.warning("Using API URL from environment: " + api_base_url)
        
        st.session_state.api_client = ApiClient(api_base_url)
    
    st.set_page_config(
        page_title="P2P Anonymous Chat",
        page_icon="💬",
        layout="wide"
    )
    
    # Render sidebar (returns active room ID)
    active_room = render_sidebar()
    
    # Main content area
    st.title("P2P Anonymous Chat")
    
    # Display chat interface if room is selected
    if active_room:
        render_chat_interface(active_room, st.session_state.user_id)
    else:
        st.info("👈 Create or join a chat room from the sidebar to start chatting anonymously.")
        
        with st.expander("About this app"):
            st.markdown("""
            ### P2P Anonymous Chat
            
            This application allows you to chat anonymously with others without requiring any registration.
            
            **Features:**
            - Create private chat rooms
            - Share room IDs with others to join
            - No personal information required
            - Messages are not stored permanently
            
            **How to use:**
            1. Create a new chat room or join an existing one
            2. Share the room ID with people you want to chat with
            3. Start chatting anonymously
            """)

if __name__ == "__main__":
    main()
