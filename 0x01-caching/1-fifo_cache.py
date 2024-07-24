#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements FIFO caching
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    print("DISCARD:", first_key)
                    del self.cache_data[first_key]
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
