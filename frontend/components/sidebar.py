import streamlit as st

def render_sidebar():
    """Render the sidebar and handle room operations"""
    with st.sidebar:
        st.title("P2P Anonymous Chat")
        
        # Initialize room_id in session state if not present
        if 'active_room' not in st.session_state:
            st.session_state.active_room = None
            
        # Join existing room
        st.subheader("Join a Room")
        join_room_id = st.text_input("Enter Room ID")
        if st.button("Join Room") and join_room_id:
            try:
                # Verify room exists
                room = st.session_state.api_client.get_room(join_room_id)
                if room:
                    st.session_state.active_room = join_room_id
                    st.success(f"Joined room {join_room_id}")
                    st.experimental_rerun()
                else:
                    st.error("Room not found")
            except Exception as e:
                st.error(f"Error joining room: {str(e)}")
                
        # Create new room
        st.subheader("Create a Room")
        if st.button("Create New Room"):
            try:
                new_room = st.session_state.api_client.create_room()
                st.session_state.active_room = new_room['room_id']
                st.success(f"Created room: {new_room['room_id']}")
                st.info("Share this room ID with others to chat together.")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error creating room: {str(e)}")
        
        # Display current room info
        if st.session_state.active_room:
            st.subheader("Current Room")
            st.info(st.session_state.active_room)
            
            # Leave room button
            if st.button("Leave Room"):
                st.session_state.active_room = None
                st.experimental_rerun()
        
        # Display user information
        st.subheader("Your Info")
        st.text(f"User ID: {st.session_state.user_id[:8]}...")
        
        # Reset user ID
        if st.button("Reset User ID"):
            import uuid
            st.session_state.user_id = str(uuid.uuid4())
            st.success("User ID reset successfully")
            st.experimental_rerun()
    
    return st.session_state.active_room
