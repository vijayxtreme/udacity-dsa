class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
                for value in init_list:
                    self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start

def iscircular(linked_list):
    """
    Determine whether the Linked list is circular or not

    Args:
        linked_list(obj): Linked List to be checked
    Returns:
        bool: Return True if the linked list is circular, return False otherwise
    """
    # traverse the list with two runners
    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head.next
    while slow.next and fast.next.next:
        if fast.value == slow.value:
            return True
        fast = fast.next.next
        slow = slow.next
    # if we finish the linked list not a loop
    return False

print(iscircular(list_with_loop))