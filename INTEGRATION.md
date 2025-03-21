# Backend Integration Guide

This document describes how to integrate the frontend with the backend API.

## Base URL

The base URL for all API requests is `/api`.

## Endpoints

### Chat Rooms

1.  **Create Chat Room**

    - **Method:** `POST`
    - **Endpoint:** `/api/chat/rooms`
    - **Request Body:** None
    - **Success Response:**

      - **Status Code:** `201`
      - **Body:**

        ```json
        {
            "data": {
                "id": integer,
                "room_id": string,
                "created_at": string
            },
            "message": "Chat room created successfully",
            "status": "success"
        }
        ```

    - **Example:**


        ```javascript
        fetch('/api/chat/rooms', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => console.log(data));
        ```

2.  **Get Chat Room**

    - **Method:** `GET`
    - **Endpoint:** `/api/chat/rooms/<room_id>`
    - **Request Body:** None
    - **Success Response:**

      - **Status Code:** `200`
      - **Body:**

        ```json
        {
            "data": {
                "id": integer,
                "room_id": string,
                "created_at": string
            },
            "message": "Chat room retrieved successfully",
            "status": "success"
        }
        ```

    - **Error Response (Room Not Found):**
    - **Status Code:** `404`
    - **Body:**

      ```json
      {
        "data": null,
        "message": "Room not found",
        "status": "error"
      }
      ```

    - **Example:**


        ```javascript
        fetch('/api/chat/rooms/your_room_id', { // Replace your_room_id
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => console.log(data));
        ```

3.  **Post Message**

    - **Method:** `POST`
    - **Endpoint:** `/api/chat/rooms/<room_id>/messages`
    - **Request Body:**

      ```json
      {
          "sender_id": string,
          "content": string
      }
      ```

    - **Success Response:**

      - **Status Code:** `201`
      - **Body:**

        ```json
        {
            "data": {
                "id": integer,
                "chat_room_id": integer,
                "sender_id": string,
                "content": string,
                "timestamp": string
            },
            "message": "Message sent successfully",
            "status": "success"
        }
        ```

    - **Error Response (Missing Fields):**
      - **Status Code:** `400`
      - **Body:**
      ```json
      {
        "data": null,
        "message": "Sender ID and content are required",
        "status": "error"
      }
      ```
    - **Example:**


        ```javascript
        fetch('/api/chat/rooms/your_room_id/messages', {  // Replace your_room_id
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                sender_id: 'user123',
                content: 'Hello, world!'
            })
        })
        .then(response => response.json())
        .then(data => console.log(data));
        ```

4.  **Get Room Messages**

    - **Method:** `GET`
    - **Endpoint:** `/api/chat/rooms/<room_id>/messages`
    - **Request Body:** None
    - **Success Response:**

      - **Status Code:** `200`
      - **Body:**

        ```json
        {
            "data": [
                {
                    "id": integer,
                    "chat_room_id": integer,
                    "sender_id": string,
                    "content": string,
                    "timestamp": string
                },
                ...
            ],
            "message": "Messages retrieved successfully",
            "status": "success"
        }
        ```

    - **Example:**


        ```javascript
        fetch('/api/chat/rooms/your_room_id/messages', { // Replace your_room_id
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => console.log(data));
        ```

## Data Models

### ChatRoom

```typescript
interface ChatRoom {
  id: number; // Internal database ID
  room_id: string; // UUID for the room
  created_at: string; // ISO format
}
```

### Message

```typescript
interface Message {
  id: number; // Internal database ID
  chat_room_id: number; // Internal database ID of the chat room
  sender_id: string;
  content: string;
  timestamp: string; // ISO format
}
```

## Error Handling

All API responses follow a consistent format:

```json
{
    "data": any | null, // The actual data, or null on error
    "message": string,  // A message describing the result
    "status": "success" | "error" // "success" for successful requests, "error" otherwise
}
```

The `status_code` will also indicate the success or failure of the request (e.g., 200 for success, 400 for client errors, 500 for server errors).

API_BASE_URL=https://chat.stefanusadri.my.id/
