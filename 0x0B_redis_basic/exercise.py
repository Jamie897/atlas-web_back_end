#!/usr/bin/env python3

import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

# Main code
if __name__ == "__main__":
    print("2 things have been annotated.")
    for param, annotation in Cache.store.__annotations__.items():
        print(f"Parameter {param} is annotated as {annotation}.")



