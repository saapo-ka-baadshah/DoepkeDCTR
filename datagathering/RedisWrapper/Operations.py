import redis
from functools import lru_cache

class Redis:
    def __init__(self, host:str="localhost", port:str="6379", db:int=0):
        self.client = redis.Redis(host=host, port=int(port), db=db)

    def store(self, id:int, data:list):


