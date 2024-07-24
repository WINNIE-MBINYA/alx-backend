#!/usr/bin/env python3
""" LRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements LRU caching
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                print("DISCARD:", oldest_key)
                del self.cache_data[oldest_key]

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
