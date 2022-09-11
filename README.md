# workers-fastAPI

## Instructions

Need to have virtualenv installed.

To work in local use `pipenv install` to create the virtual environment. Then work as usual.

For using the app:

```
docker-compose build
```

```
docker-compose up
```

## Celery 

Celery is a usefull tool in python for implementing cronjobs with workers. You can specify it's broker in requirements.txt. The usual flow is shown in the image:

![](docs/celery-flow.png)

You can check all the configurations in the folder `/celery-config`.
