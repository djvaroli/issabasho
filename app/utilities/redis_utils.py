import os
import json

from redis import ConnectionPool, Redis

from app.utilities.pydantic_models import *

REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")


def get_redis_client():
    return Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def store_haiku_rating(
        haiku_data: SaveHaikuRequest,
):
    redis = get_redis_client()
    hash_name = "haiku-rating-v1"
    key = haiku_data.timestamp
    haiku_data_str = json.dumps(haiku_data.dict())

    return redis.hset(hash_name, key, haiku_data_str)

