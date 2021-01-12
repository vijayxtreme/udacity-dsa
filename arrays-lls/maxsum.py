'''
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

**Example 1:**
* `arr= [1, 2, 3, -4, 6]`
* The largest sum is `8`, which is the sum of all elements of the array.

**Example 2:**
* `arr = [1, 2, -5, -4, 1, 6]`
* The largest sum is `7`, which is the sum of the last two elements of the array.
'''

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    # sum all the numbers in the array - that's the start max
    # then look at the max number in the array and work backwards, if less than max, reject
    # recurse
    max_sum = arr[0]
    sum = arr[0]
    for item in arr[1:]:
        sum = max(sum + item, item)
        max_sum = max(sum, max_sum)

    return max_sum
        
    

arr = [1, 2, 3, -4, 6]
print(max_sum_subarray(arr))

arr2 = [1, 2, -5, -4, 1, 6]
print(max_sum_subarray(arr2))
