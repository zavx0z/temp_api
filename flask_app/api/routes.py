import logging

import requests
from flask import request, jsonify

from flask_app import socketio, celery
from flask_app.api import api
from flask_socketio import send, emit

from selen_task import yt_query


@celery.task()
def query_data(data):
    yt_query(data)
    logging.info(f"run celery {data}")


@api.route('/', methods=['POST'])
def api_entry_point():
    print(request.json)
    send(request.json, namespace='/', broadcast=True)
    return {"success": "ok"}


@api.route('/task', methods=['POST'])
def run_task():
    msg = request.json.get("query")
    query_data.delay(msg)
    return jsonify({"success": "ok", "msg": msg})


@socketio.on('message')
def handle_message(message):
    print('message')
    send(message)


@socketio.on('json')
def handle_json(json):
    print('message')
    send(json, json=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('message')
    emit('my response', json)
