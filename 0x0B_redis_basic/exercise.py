#!/usr/bin/env python3

import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        # Store an instance of the Redis client as a private variable named _redis
        self._redis = redis.Redis()
        # Flush the Redis instance using flushdb
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        # Store the input data in Redis using the random key
        self._redis.set(key, data)
        # Return the key
        return key

# Main code
if __name__ == "__main__":
    print("2 things have been annotated.")
    for param, annotation in Cache.store.__annotations__.items():
        print(f"Parameter {param} is annotated as {annotation}.")



