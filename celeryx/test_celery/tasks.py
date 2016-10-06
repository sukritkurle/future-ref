from __future__ import absolute_import
from test_celery.celery import app
import time
from test_celery.db_connect import connection

@app.task
def hourly_test_scheduler():
    c, conn = connection()
    data = c.execute("select test_name from tests where frequency='hourly'")
    data = c.fetchall()
    conn.close()

    for test in data:
        print "RUNNING HOURLY TEST {}".format(test[0])

@app.task
def daily_test_scheduler():
    c, conn = connection()
    data = c.execute("select test_name from tests where frequency='daily'")
    data = c.fetchall()
    conn.close()

    for test in data:
        print "RUNNING DAILY TEST {}".format(test[0])

@app.task
def weekly_test_scheduler():
    c, conn = connection()
    data = c.execute("select test_name from tests where frequency='weekly'")
    data = c.fetchall()
    conn.close()

    for test in data:
        print "RUNNING WEEKLY TEST {}".format(test[0])
