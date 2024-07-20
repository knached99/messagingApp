"""
@author: Khaled
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", manage_session=False)  # `manage_session=False` is recommended for better performance

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('home'))

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info(f"{data['username']} has sent message to the room {data['room']}: {data['message']}")
    socketio.emit('receive_message', data, room=data['room'])

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
    # Ensure you use `host='0.0.0.0'` for external access or leave it as default for local access
    socketio.run(app, debug=True, host='0.0.0.0')
