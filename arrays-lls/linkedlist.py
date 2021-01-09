"""
Implement a linked list class. You have to define a few functions that perform the desirable action. Your LinkedList class should be able to:

* Append data to the tail of the list and prepend to the head
* Search the linked list for a value and return the node
* Remove a node
* Pop, which means to return the first node's value and delete the node from the list
* Insert data at some position in the list
* Return the size (length) of the linked list
"""

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
    
class LinkedList: 
    def __init__(self):
        self.head = None 
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            head = self.head
            self.head = Node(value)
            self.head.next = head

    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head == None:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            # at last node            
            curr.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        curr = self.head 
        while curr:
            if curr.value == value:
                return curr
            print(curr.value)
            curr = curr.next
        
        return None

    def remove(self, value):
        if self.head == None:
            return None

        if self.head.value == value:
            self.head = self.head.next
            return self.head
        else:
            curr = self.head
            while curr:
                if curr.next:
                    if curr.next.value == value:
                        if curr.next.next:
                            curr.next.value = curr.next.next.value
                            curr.next.next = curr.next.next.next
                            break
                        else:
                            curr.next = None
                            break
                curr = curr.next
            return self.head

    def pop(self):
        if self.head.next:
            head = self.head
            self.head = self.head.next
            return head
        else:
            head = self.head 
            self.head = None
            return head
        

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the length of the list, append to the end of the list. """
        if pos < 0:
            return self.head 

        if self.head == None:
            self.head = Node(value)
            return self.head
        
        count = 0
        ins = pos - 1
        curr = self.head 
        while curr:
            
            if count == ins:
                prev = curr.next
                curr.next = Node(value)
                curr.next.next = prev
                return self.head
            count += 1
            curr = curr.next
        
        self.append(value)

        return self.head        

    def size(self):
        curr = self.head
        count = 0
        if self.head is None:
            return count
        while curr:
            count += 1
            curr = curr.next
        return count

linked_list = LinkedList()
linked_list.prepend(0)
# print(linked_list.to_list() == [1])
# print(linked_list.to_list())
linked_list.append(3)
linked_list.append(3)
linked_list.append(3)
linked_list.append(1)
linked_list.append(3)
linked_list.append(4)
# linked_list.prepend(0)
# print(linked_list.to_list())
# found = linked_list.search(1)
# print(found.value)
# found = linked_list.search(4)
# print(found.value)
# try: 
#     print(found.value)
# except:
#     print("None value returned")
# linked_list.remove(1)
# linked_list.remove(4)
# a = linked_list.pop()
# print(a.value)
# b = linked_list.pop()
# print(b.value)
print(linked_list.to_list())
linked_list.insert(5,3)
print(linked_list.to_list())
# print(linked_list.size())
