#!/usr/bin/env python3
""" LFUCache module
"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements LFU caching
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = defaultdict(int)
        self.use_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
            else:
                if (len(self.cache_data) >= self.MAX_ITEMS):
                    lfu_keys = [
                        k for k, v in self.frequency.items()
                        if v == min(self.frequency.values())
                    ]
                    if len(lfu_keys) > 1:
                        oldest_key = next(
                            k for k in self.use_order if k in lfu_keys
                        )
                    else:
                        oldest_key = lfu_keys[0]
                    print("DISCARD:", oldest_key)
                    del self.cache_data[oldest_key]
                    del self.frequency[oldest_key]
                    self.use_order.remove(oldest_key)
                self.frequency[key] = 1
                self.use_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.frequency[key] += 1
            index = self.use_order.index(key)
            self.use_order.append(self.use_order.pop(index))
            return self.cache_data[key]
        return None
