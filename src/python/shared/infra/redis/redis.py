from decouple import config

from src.python.shared.infra.redis.redis_handler import Redis

REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT')
REDIS_PASSWORD = config('REDIS_PASSWORD')

redis_instance = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
)
