from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #cache list is the DoublyLinkedList
        self.cache = DoublyLinkedList()
        #set the limit to whatever is specified (defaults to 10)
        self.limit = limit
        #size starts at 0
        self.size = 0
        #sets storage to an empty key/value pair
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #if the specified key is in the storage, set the node to the key in storage, then move the node to the head so it is considered used most recently and return the value (which is at index 1, as the key is at index 0)
        if key in self.storage:
            node = self.storage[key]
            self.cache.move_to_front(node)
            return node.value[1]
        else:
            return None
        

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
        #if the specified key is in the storage, overwrite with the new value and bump it to the head as it was most recently used
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.cache.move_to_front(node)
            return
        #if the limit has already been reached, delete the tail key/value pair and decrease size by one
        if self.size == self.limit:
            del self.storage[self.cache.tail.value[0]]
            self.cache.remove_from_tail()
            self.size -=1
        #add the new key/value pair to the head and increase size by 1
        self.cache.add_to_head((key, value))
        self.storage[key] = self.cache.head
        self.size += 1
