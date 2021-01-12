'''
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list where all even elements are odd elements
    """