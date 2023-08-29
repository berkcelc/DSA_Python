# writing factorial using recursion 

import sys
sys.setrecursionlimit(10000)

"""
We have a limit of stack memory if the recursion 
goes into infinite loop 

in case we have a deep recursive function, we 
can set the depth of the recursion stack

We can use assert method to validate the input the values
"""

def factorial(num):
    assert num>=0 and int(num) == num, 'The input must be a positive integer' 
    if num < 0:
        return None
    if num in [0,1]:
        return 1
    else:
        return factorial(num - 1) * num


