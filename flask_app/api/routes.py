from flask_app import socketio
from flask_app.api import api
from flask_socketio import send, emit


@api.route('/', methods=['GET'])
def api_entry_point():
    return {"success": "ok"}


@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('json')
def handle_json(json):
    send(json, json=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)
