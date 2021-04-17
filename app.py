from celery import Celery
import config
import redis
from os import environ

app = Celery(__name__)
app.config_from_object(config)
app.conf.redisClient = redis.Redis(
    host=environ.get("REDIS_HOST"),
    password=environ.get("REDIS_PASSWORD"),
    port=environ.get("REDIS_PORT"),
    db=environ.get("REDIS_DB")
)

if environ.get("TABLE_SIMULATION"):
    from task import tableSimulation
