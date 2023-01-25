#!/usr/bin/python3
''' class FIFOCache that inherits from BaseCaching '''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' class '''

    def __init__(self):
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        ''' assign to the dict self.cache_data the item value for the key
        if key or item is None, this smethod shouldnt do anyting
        if number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS
        - you dicard the first item put in Cache '''
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        ''' returns the value in self.cache_data linked to key '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
