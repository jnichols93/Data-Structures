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
        #set the limit to whatever is specified (defaults to 10)
        self.limit = limit
        #size starts at 0
        self.size = 0
        #sets storage to an empty key/value pair
        self.storage = {}
        #cache list is the DoublyLinkedList
        self.order = DoublyLinkedList()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If key is in storage
        if key in self.storage:
            # move it to the end
            node = self.storage[key]
            self.order.move_to_end(node)
            # return the value
            return node.value[1]
        # if not
        else:
            # return none
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
        # check and see if the key is in the dict
        if key in self.storage:
            # If it is
            node = self.storage[key]
                # overwrite the value
            node.value = (key, value)
                # move it to the end
            self.order.move_to_end(node)
            # nothing else to do, exit the function
            return

        # check and see if cache is full
        if self.size == self.limit:
            # if cache is full
            # remove oldest entry from dictionary
            del self.storage[self.order.head.value[0]]
                # AND  Linked-List
            self.order.remove_from_head()
                # reduce the size
            self.size -= 1

        # add to linked list(key and the value)
        self.order.add_to_tail((key, value))
        # add the key and value to the dictionary
        self.storage[key] = self.order.tail
        # increment size
        self.size += 1