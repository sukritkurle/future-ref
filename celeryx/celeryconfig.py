import time
from celery.task.schedules import crontab
from datetime import datetime, timedelta

BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_IMPORTS = ['test_celery.tasks']

CELERYBEAT_SCHEDULE={
    'Daily_Test_Scheduler':{
        'task':'test_celery.tasks.daily_test_scheduler',
        'schedule': timedelta(seconds=10)
    },

    'Hourly_Test_Scheduler':{
        'task':'test_celery.tasks.hourly_test_scheduler',
        'schedule': timedelta(seconds=15),
    },

    'Weekly_Test_Scheduler':{
        'task':'test_celery.tasks.weekly_test_scheduler',
        'schedule': crontab(minute=''),
    }
}
