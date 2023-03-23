import redis


class Redis(object):
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0,
                 password: str = None, socket_timeout: int = None):
        print('[REDIS] Connecting to redis')
        self.connection = redis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            socket_timeout=socket_timeout
        )

    def get(self, key: str) -> bool:
        if self.exists(key):
            return False
        self.connection.get(key)
        return True

    def set(self, key: str, value: str) -> bool:
        if self.exists(key):
            self.connection.set(key, value)
            return True
        return False

    def exists(self, key: str) -> bool:
        result = self.connection.exists(key)
        if result == 0:
            return False
        return True
