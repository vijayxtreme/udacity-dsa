"""
You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete the next j nodes. Continue doing so until the end of the linked list.

Example:

linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12
"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    i_count = 1
    curr = head
    while curr:
        if i_count % i == 0:
            j_count = 0
            while j_count < j and curr.next:
                curr.next = curr.next.next
                j_count += 1
        i_count += 1
        curr = curr.next

    return head

ll = create_linked_list([1,2,3,4,5,6])
ll = skip_i_delete_j(ll, 2, 3)
print_linked_list(ll)