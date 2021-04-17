from celery import shared_task, current_app
from time import sleep


@shared_task(bind=True)
def tableSimulation(self, event, eventTime, revenue, **kwargs):
    sleep(eventTime)
    return revenue
