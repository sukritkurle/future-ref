from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery')
app.config_from_object('celeryconfig')
