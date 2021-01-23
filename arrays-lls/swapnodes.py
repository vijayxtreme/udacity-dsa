"""
Given a linked list, swap the two nodes present at position i and j, assuming 0 <= i <= j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

linked_list = 3 4 5 2 6 1 9
positions = 2 5
output = 3 4 1 2 6 5 9
Explanation:

The node at position 3 has the value 2
The node at position 4 has the value 6
Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9
"""

class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None

"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""
def swap_nodes(head, left_index, right_index):
    curr = head # get head, make a pointer to it
    temp1 = None #node before swap1
    temp2 = None #node before swap2
    swap1 = None
    swap2 = None 

    if head.data == left_index:
        #if we're at the head and we have a swap, move head
        swap1 = head

    while curr: #look at each next node

        if curr.next and curr.next.data == left_index:
            temp1 = curr
            swap1 = curr.next
        
        if curr.next and curr.next.data == right_index:
            temp2 = curr
            swap2 = curr.next
   
        curr = curr.next #get the next 

    if not swap1 or not swap2:
        return head
    
    # else do the swap, 3 and 4 are temp1 and temp2, 5 and 1 are swap1 and swap2
    if swap1 == head:
        save = swap2.next
        head = swap2
        head.next = swap1
        swap1.next = save

    else:
        save = swap2.next # save swap2.next to use at end 9
        temp1.next = temp2.next #4 points to 1 (6's next) - swapping
        swap2.next = swap1.next #1 points to 2 (5's next)
        temp2.next = swap1 #6's next points to 5 now -- swapping
        swap1.next = save # 5's next is 9 (temp2's original next)

    return head
    '''
    3-4-5-2-6-1-9
    5 and 1 get replaced
    '''

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
        print(head.data, end=" ")
        head = head.next
    print()


arr = [3, 4, 5, 2, 6, 1, 9]
print(arr)
head = create_linked_list(arr)
left_index = 3
right_index = 4
head = swap_nodes(head, left_index, right_index)
print_linked_list(head)

