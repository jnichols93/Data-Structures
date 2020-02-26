# think binary trees but ordered by breadth 
"""
resources used:
https://www.guru99.com/stack-vs-heap.html,

"""
class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        if comparator:
            self.comparator = comparator
        else:
            # lambda assignment resources https://realpython.com/python-lambda/ 
            # Unlike lambda forms in other languages, where they add functionality, 
            # Python lambdas are only a shorthand notation if you’re too lazy to define a function.
            self.comparator = lambda a, b: a > b

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(-1)

    def delete(self):
        # swap first and last
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        current_priority = self.storage.pop()
        # sift down new root
        if self.get_size():
            self._sift_down(0)
        return current_priority

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # allow negative index
        if index < 0:
            index += self.get_size()
        # compare with parent, and swap if True
        parent = (index-1)//2
        if self.comparator(self.storage[index], self.storage[parent]):
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            # if not index 0, keep bubbling
            if parent:
                self._bubble_up(parent)

    def _sift_down(self, index):
        # allow negative index
        if index < 0:
            index += self.get_size()
        # compare children and swap if True
        index_a = 2*index + 1
        index_b = 2*index + 2
        parent = self.storage[index]
        child_a = None
        try:
            child_a = self.storage[index_a]
            child_b = self.storage[index_b]
        except IndexError:
            if child_a and self.comparator(child_a, parent):
                self.storage[index], self.storage[index_a] = self.storage[index_a], self.storage[index]
                self._sift_down(index_a)
            return
        if self.comparator(child_a, child_b):
            if self.comparator(child_a, parent):
                self.storage[index], self.storage[index_a] = self.storage[index_a], self.storage[index]
                self._sift_down(index_a)
                return
        else:
            if self.comparator(child_b, parent):
                self.storage[index], self.storage[index_b] = self.storage[index_b], self.storage[index]
                self._sift_down(index_b)
                return