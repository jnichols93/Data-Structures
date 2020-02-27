import os
import sys

queue_stack_path = os.path.normpath(os.path.join(__file__, '../../queue_and_stack'))
sys.path.append(queue_stack_path)

from dll_queue import Queue
from dll_stack import Stack

#lru_cache(maxsize=500) 
#least recently used (will purge if not lrc)
#wraps another function HOC - behind the scenes
#takes form of key value pairs
#keep track of priority order can use other DS to help with this
#MRU etc many types

#hints: single nodes can still be binary search trees
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node #VALUE IS LESS THAN CURRENT NODE (SELF.VALUE)
        if value < self.value:
            # if there is no self.left value: 
            if not self.left:
                # set the new left child to be new value
                self.left = BinarySearchTree(value) #creates new intance of BInarySearchTree node with (self.value as root, has self.left & self.right)
            else: #if self.left exists:
                self.left.insert(value) #recurse call insert on the self.left node (which exists) and does comparison steps above to  value / repeats the process above 
        # NEW VALUE IS GREATER THAN CURRENT NODE (SELF.NODE):
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value) #(CREATE NEW BST)
            else: 
                self.right.insert(value)#RECURSE, THE SELF.RIGHT NODE AND RECURSE THE COMPARISON LOGIC
# Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True    
        # target is smaller, go left
        sub_tree_contains = False
        if target < self.value:
            if not self.left:
                return False
            else:
                sub_tree_contains = self.left.contains(target) #IMPORTANT RETURN can be used here b/c `contains` function ASKING FOR RETURN BOOLEAN (INSTEAD OF ADDING NODE)
        # target is greater, go right
        else:
            if not self.right:
                return False
            else:
                sub_tree_contains = self.right.contains(target)
        return sub_tree_contains
    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        # recursive solution
        # if we can go right, go right
        # return when we can't go right anymore
        # if not self.right: (NOTHING TO RIGHT, SO NOTHING LARGER THAN ROOT NODE SO MAX IS ROOT NODE )
        #     return self.value    
        # return self.right.get_max()
        
        # iterative solution
        current_tree_root = self
        while current_tree_root.right: # can also be while current_tree_root is not None: 
            current_tree_root = current_tree_root.right #REMEMBER THIS MOVES CURR TO THE RIGHT POSITION AS THE NEW CURR 

        return current_tree_root.value

    # Call the function `cb` on the value of each node #cb= another function 
    # You may use a recursive or iterative approach
    def for_each(self, cb): #EX OF DFS, PATH WE CHOOSE WE GO ALL THE WAY AND VISIT (ORDER IS 8, 4, 6)
        cb(self.value)    
#STACK nothing goes until every function on top level is done, then next on the stack is executed 
        if self.left:
            self.left.for_each(cb) #recurse for_each #waits for this to finish before if self.right called 
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
