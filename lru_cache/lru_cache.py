from collections import OrderedDict
# OrderedDict works the same as a dict, but keeps a timestamp of all the entries. Updating data won't move it's stack position but removing and readding it will put it at the end

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = OrderedDict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Determine if key exists in the cache
        # If not, return None
        # If it does, pop and update cache with the data to put it at the back
        if key not in self.cache:
            return None
        else:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Add, or update if it exists, the key with the value
        self.cache[key] = value
        # If the length is not over the limit, remove the oldest entry
        if len(self.cache) > self.limit:
            self.cache.popitem(last=False)
