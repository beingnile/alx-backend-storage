#!/usr/bin/env python3

"""Defines a class cache
"""

import uuid
import redis
from typing import Union


class Cache:
    """Stores information in a redis cache
    """
    def __init__(self):
        """Instantiate a Redis client and flush the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates random key and stores the input
        data in Redis using the random key

        Args:
            data: The input data

        Returns:
            The random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
