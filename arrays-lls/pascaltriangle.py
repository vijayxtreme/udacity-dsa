'''
Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.

For example, if n = 4, then output = [1, 4, 6, 4, 1].

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html
'''

def nth_row_pascal(n):
    '''
    pascal works in 11^n, so just have to get the value and create an array
    tricky stuff is when we go over 5 -- then we have to do something more manual,
    hence no easy answer for this.

    o(n^2) -- for now i'm okay with this.  i'll explore later, move on.
    '''

    pass