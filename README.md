### Flask-SocketIO
[documentation](https://flask-socketio.readthedocs.io/en/latest/)
### Flask-Migrate
[documentation](https://flask-migrate.readthedocs.io/en/latest/)
```bash
flask db init
flask db migrate -m "message"
flask db upgrade
flask db downgrade
```
### celery
* start
```bash
celery -A flask_app.celery worker --loglevel=info
```