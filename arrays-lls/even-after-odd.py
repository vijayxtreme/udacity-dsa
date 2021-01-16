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
    def get_tail(head):
        curr = head
        # get tail
        while curr.next:
            curr = curr.next 
        tail = curr
        return tail

    def set_tail(head, node):
        curr = head
        node.next = None
        while curr.next:
            curr = curr.next
        tail = curr
        tail.next = node

    def get_length(head):
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count +=1
        return count

    end = get_tail(head)
 
    while head != end:
        if head.data % 2 == 0:
            node = head 
            head = head.next
            set_tail(head, node)
        else:
            break

    if head.data % 2 == 0:
        node = head 
        head = head.next
        set_tail(head, node)

    # print_linked_list(head)
    # 1-2-3-4-5-6
    curr = head # tail
    end = get_tail(head)
    
    while curr.next and curr.next != end:
        if curr.next.data % 2 == 0:
            node = curr.next # 2 copy
            curr.next = node.next # 3
            set_tail(head, node)
        else:
            curr = curr.next

    if curr.next == end:
        if end.data % 2 == 0:
            node = curr.next 
            curr.next = node.next
            set_tail(head, node)
    
    # end = get_tail(head) 
    # print(get_length(head))
    return head

    

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

ll = create_linked_list([1,2,3,4,5,6,7,8])

ll = even_after_odd(ll)

print_linked_list(ll)