import logging

from flask import request

from flask_app import socketio, celery
from flask_app.api import api
from flask_socketio import send, emit


@api.route('/', methods=['GET'])
def api_entry_point():
    return {"success": "ok"}


@celery.task()
def task(data):
    logging.info(f"run celery {data}")


@api.route('/task', methods=['POST'])
def run_task():
    msg = request.json.get("task")
    task.delay(msg)
    return {"success": "ok", "msg": msg}


@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('json')
def handle_json(json):
    send(json, json=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)
