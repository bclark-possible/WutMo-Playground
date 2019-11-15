import redis
from storage.SimpleDataStorage import SimpleDataStorage

'''
Data Storage via redis
https://redislabs.com/get-started-with-redis/
'''
class SimpleRedisStorage(SimpleDataStorage):
    connection = None

    def __init__(self, host, port):
        print("Creating redis connection{0}:{1}".format(host,int(port)))
        self.connection = redis.Redis(host=host, port=port)
        print("Pinging connection")
        self.connection.ping()

    def set(self, key, value):
        if self.connection is not None:
            self.connection.set(key, value)
            return (key,value)
        return None
    
    def get(self, key):
        if self.connection is not None:
            return self.connection.get(key)
        return None
        