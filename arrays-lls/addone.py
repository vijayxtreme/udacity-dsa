'''
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [1, 2, 9]
output = [1, 3, 0]
Example 3:

input = [9, 9, 9]
output = [1, 0, 0, 0]
Challenge: One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.

But can you solve it in some other way?
'''
def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits representing (x+1)
    """

    carry = False
    arr[len(arr)-1] += 1

    for i in range(len(arr)-1, -1, -1):
        if carry:
            arr[i] += 1
            carry = False
        if arr[i] == 10 or arr[i] + 1 == 10:
            arr[i] = 0
            carry = True
        # Then we can break out early from loop 
        # making this function even faster
        if not carry:
            break

    if carry:
        return [1] + arr
    
    return arr 

A = [1,0,0]
B = [9,9,9]
print(add_one(A))