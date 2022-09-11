import os
from dotenv import load_dotenv

# FastAPI
from fastapi import FastAPI

# celery
from celery import Celery
from celery_config.tasks import wait_and_return

load_dotenv('.env')

app = FastAPI()

celery_app = Celery(
    __name__,
    # https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html
    broker=os.environ.get('CELERY_BROKER_URL', ''),
    backend=os.environ.get('CELERY_RESULT_BACKEND', '')
)

# Setup to use all the variables in settings
# that begins with 'CELERY_'
celery_app.config_from_object('celery_config.config', namespace='CELERY')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/job/")
def get_execute_job():
    wait_and_return.delay()
    return {"job": "executed"}
