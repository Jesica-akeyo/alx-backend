#!/usr/bin/python3
''' a class BasicCache that inherits from BaseCaching '''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' class BasicCache that inherits from BaseCaching and is a 
    caching system '''

    def put(self, key, item):
        ''' assign to the dict self.cache_data the item value for thw key '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' return the value in self.cache_data linked to key '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
