'''
You have been given an array of length = n. **The array contains integers from 0 to n - 2**. Each number in the array is **present exactly once except for one number which is present twice**. Find and return this duplicate number present in the array

Example:

arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)
The expected time complexity for this problem is O(n) and the expected space-complexity is O(1).
'''

def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    '''
    Since the numbers are all unique, we can sum them all up to n-2. 
    The duplicate number is the number that is the difference of the sum and
    the sum of the numbers in this array
    '''
    k = len(arr)-1
    expected_sum = (k*(k-1))//2 #(n)(n-1)/2 (sum of all numbers up to n)
    sum = 0
    for item in arr:
      sum += item

    difference = int(sum - expected_sum)
    print(expected_sum, difference, sum)
    return difference

arr = [0, 2, 3, 1, 4, 5, 3]

print(duplicate_number(arr))
