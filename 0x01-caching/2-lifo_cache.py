#!/usr/bin/python3
''' self descriptive code '''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' assign to dict self.cahe_data the item value for the key
    if no of items in self.cache_data is higher than BaseCaching.MAX_ITEMS
    - discard the last item put in cache '''

    def __init__(self):
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        ''' self descriptive '''
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        ''' returns the value in self.cache_data linked to key '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None