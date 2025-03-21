import streamlit as st
import time

def render_chat_interface(room_id, user_id):
    """Render the chat interface for a specific room"""
    st.header(f"Chat Room: {room_id}")
    
    # Initialize messages in session state if not present
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        
    # Load messages from API
    with st.spinner("Loading messages..."):
        try:
            messages = st.session_state.api_client.get_messages(room_id)
            # Update session state with messages from API
            st.session_state.messages = messages
        except Exception as e:
            st.error(f"Error loading messages: {str(e)}")
            st.session_state.messages = []
    
    # Chat container for messages
    chat_container = st.container()
    
    # Define a callback for message sending
    def send_message():
        if st.session_state.message_input:
            try:
                new_message = st.session_state.api_client.send_message(
                    room_id,
                    user_id,
                    st.session_state.message_input
                )
                st.session_state.messages.append(new_message)
                st.session_state.message_input = ""  # Clear input
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error sending message: {str(e)}")
    
    # Input for new messages
    with st.container():
        col1, col2 = st.columns([5, 1])
        with col1:
            # Add on_change parameter to handle Enter key presses
            message_input = st.text_input("Type your message:", key="message_input", on_change=send_message)
        with col2:
            send_btn = st.button("Send", on_click=send_message)
    
    # Display messages
    with chat_container:
        if not st.session_state.messages:
            st.info("No messages yet. Be the first to send one!")
        else:
            for message in st.session_state.messages:
                is_user = message['sender_id'] == user_id
                message_container = st.container()
                
                with message_container:
                    cols = st.columns([1, 4])
                    with cols[0]:
                        # Show "You" for the user's messages, otherwise show a masked ID
                        if is_user:
                            st.text("You")
                        else:
                            # Use first 6 chars of sender_id to create a consistent but anonymous identity
                            sender_short_id = message['sender_id'][:6]
                            st.text(f"User {sender_short_id}...")
                    with cols[1]:
                        message_box = st.container()
                        with message_box:
                            st.markdown(f"<div style='background-color:{'#DCF8C6' if is_user else '#F1F0F0'}; padding:10px; border-radius:10px;'>{message['content']}</div>", unsafe_allow_html=True)
                            st.caption(f"{message['timestamp']}")
    
    # Auto refresh chat (every 5 seconds)
    auto_refresh = st.checkbox("Auto refresh", value=True)
    if auto_refresh:
        st.empty()
        time.sleep(5)
        st.experimental_rerun()
