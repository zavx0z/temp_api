import logging

from flask import request, jsonify

from flask_app import socketio, celery
from flask_app.api import api
from flask_socketio import send, emit
import requests


@celery.task()
def query_data(data):
    r = requests.post('http://localhost:5000/api/', {data: data})
    logging.info(f"run celery {data}")


@api.route('/', methods=['POST'])
def api_entry_point():
    data = request.json.get('data')
    print(data)
    return {"success": "ok"}


@api.route('/task', methods=['POST'])
def run_task():
    msg = request.json.get("query")
    query_data.delay(msg)
    return jsonify({"success": "ok", "msg": msg})


@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('json')
def handle_json(json):
    send(json, json=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)
