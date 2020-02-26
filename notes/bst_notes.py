"""BINARY SEARCHES 
COMPLEXITY (LOG N)
-------------------- Pseudo code --------------------
insert value:
# base case -> if there is no node at root
# insert this as root
# comapare value to the root
# if value is smaller:
#     look left if node, repeat steps
#     if no node: make a new one with this value
# if value is greater or equal
#     look right, if node repeat steps
#     if no node: make a new one with this value

find value:
# base case-> if no node at root return False
# otherwise comare value to root
# if smaller:
#     go left look at node there
# if greater or ==:
#     go right

get max:
# base case -> if no right child, return this value
#  otherwise go right.
# """