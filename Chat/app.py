from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", manage_session=False)

# Generate a key for encryption
encryption_key = os.urandom(32)  # AES-256 key
iv = os.urandom(16)  # AES block size for CBC mode
cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend())

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html', username=username, room=room, encryption_key=base64.b64encode(encryption_key).decode(), iv=base64.b64encode(iv).decode())
    else:
        return redirect(url_for('home'))

@socketio.on('send_message')
def handle_send_message_event(data):
    try:
        app.logger.info(f"Received encrypted message: {data['message']}")
        encrypted_message = base64.b64decode(data['message'])
        decryptor = cipher.decryptor()
        decrypted_padded_message = decryptor.update(encrypted_message) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()
        decrypted_message_str = decrypted_message.decode('utf-8')
        app.logger.info(f"Decrypted message: {decrypted_message_str}")
        data['message'] = decrypted_message_str
        socketio.emit('receive_message', data, room=data['room'])
    except Exception as e:
        app.logger.error(f"Error decrypting message: {e}")

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info(f"{data['username']} has joined the room {data['room']}")
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])

@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info(f"{data['username']} has left the room {data['room']}")
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
