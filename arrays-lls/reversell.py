class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
        
    def __repr__(self):
        return str([v for v in self])

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(repr(ll.__repr__()))

def reverse(linked_list):
    new_ll = LinkedList()
    prev = None 
    for item in linked_list:
        node = Node(item)
        node.next = prev
        prev = node
    new_ll.head = prev
    return new_ll

print(reverse(ll))

# def ll_reverse(linked_list):
#     ll_reverse = LinkedList()
#     ll_to_list_reverse = eval((repr(linked_list)))[::-1]

#     for item in ll_to_list_reverse:
#         ll_reverse.append(item)
#     return ll_reverse

# print(ll_reverse(ll))
