# messagingApp

**Instant Messaging Web Application**

This is an instant chat application which utilizes Flask and Flask-SocketIO for real-time communication, and the `cryptography` library for implementing end-to-end encryption (E2EE) to ensure message confidentiality. Below is a detailed explanation of the encryption algorithm used.

## Features

- **Real-Time Messaging:** Exchange messages instantly with other users in the same chat room.
- **Encryption:** Messages are encrypted to ensure privacy.
- **Session Management:** Join or leave chat rooms and view announcements for these actions.


## Encryption Algorithm

### Advanced Encryption Standard (AES)

The encryption algorithm used in this application is the Advanced Encryption Standard (AES), specifically AES-256 in Cipher Block Chaining (CBC) mode with PKCS7 padding. 

### Key Points of AES-256

1. **Key Size**: AES-256 uses a 256-bit key, making it highly secure against brute-force attacks.
2. **Block Size**: AES operates on fixed block sizes of 128 bits.
3. **Mode of Operation**: Cipher Block Chaining (CBC) mode is used to enhance the security of AES by ensuring that identical plaintext blocks yield different ciphertext blocks.


### Steps of the Encryption Process

1. **Key Generation**: A 256-bit key is generated using a secure random number generator.
2. **Initialization Vector (IV)**: A 128-bit IV is generated to ensure that the same plaintext encrypts to different ciphertext in different encryption sessions.
3. **Padding**: PKCS7 padding is applied to the plaintext to ensure it is a multiple of the block size.
4. **Encryption**: The plaintext is encrypted using AES-256 with the generated key and IV in CBC mode.

### Steps of the Decryption Process

1. **Decryption**: The ciphertext is decrypted using the same key and IV used during encryption.
2. **Unpadding**: PKCS7 padding is removed to retrieve the original plaintext.


## Getting Started

Follow these steps to set up and run the application locally:

### 1. Clone the Repository

```bash
git clone https://github.com/knached99/messagingApp.git
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