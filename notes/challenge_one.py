# UPER
# given an sll how can we find the middle only going over once.
# RABBIT AND HARE METHOD
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node
    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
def midpoint(root):
    hare = root.head
    turtle = root.head
    while hare.next:
        if hare.next.next is None:
            return turtle.value
    hare = hare.next.next
    turtle = turtle.next
    return turtle.value