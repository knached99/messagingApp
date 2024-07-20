# messagingApp

**Instant Messaging Web Application**

This is an instant messaging web application built with Flask, a Python web development framework, and Socket.io for real-time socket communication. The primary goal is to enhance security by minimizing the risk of packet capture using tools like WireShark.

## Features

- **Real-Time Messaging:** Exchange messages instantly with other users in the same chat room.
- **Encryption:** Messages are encrypted to ensure privacy.
- **Session Management:** Join or leave chat rooms and view announcements for these actions.

## Getting Started

Follow these steps to set up and run the application locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/messagingApp.git
```

### 2. Navigate to the Project Directory
```bash
cd messagingApp
```
### 3. Set Up a Virtual Environment
For Windows:

```bash 
python -m venv venv
.\venv\Scripts\activate.ps1

```

For Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate

```

### 4. Install Dependencies
Navigate to the chat directory and install the required Python packages:

```bash
cd chat
pip install -r requirements.txt

```

### 5. Run the Application
Start the Flask server:

```bash
python app.py

```

### 6. Accessing the Application
Open your browser and go to http://localhost:5000.

### 7. Using the Application
Enter Username and Room Number: In the browser, input your desired username and room number to start a chat session.
Join from Another Tab: Open a new tab or browser window, enter a different username but the same room number to join the same chat room.
Configuration
Secret Key: The application uses a dynamically generated secret key for message encryption. Ensure to handle this key securely.
Notes
Ensure your environment meets the requirements specified in requirements.txt.
For any issues or feature requests, please open an issue on the GitHub repository.