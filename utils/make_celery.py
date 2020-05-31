from celery import Celery


def make_celery(app):
    print(app.config['CELERY_BROKER_URL'])
    cl = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config["CELERY_BROKER_URL"]
    )
    cl.conf.update(app.config)

    class ContextTask(cl.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    cl.Task = ContextTask
    return cl
