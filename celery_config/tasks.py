# celery
from celery import shared_task

# standard
import time

# The "shared_task" decorator allows creation
# of Celery tasks for reusable apps as it doesn't
# need the instance of the Celery app.
# @celery_app.task()
@shared_task()
def add(x, y):
    return x + y

@shared_task
def kenobi():
    print("Hello there!")

@shared_task
def grievous():
    print('General Kenobi!')

@shared_task
def wait_and_return():
    time.sleep(20)
    return 'Hello World!'