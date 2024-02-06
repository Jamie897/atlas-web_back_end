#!/usr/bin/env python3

import redis
import functools

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key):
        data = self._redis.get(key)
        if data is None:
            return None
        return data

def count_calls(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Get the qualified name of the method
        key = method.__qualname__
        # Increment the count for that key
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    return wrapper

# Example usage:
cache = Cache()

@count_calls
def example_method(cache_instance):
    return "Example method called"

# Call the method multiple times
for _ in range(5):
    print(example_method(cache))
