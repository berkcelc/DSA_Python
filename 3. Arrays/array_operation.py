from array import *

# create and traverse through the array

my_array = array('i',[1,2,3,4,5])

for i in my_array:
    print(i)


my_array.append(1)

my_array.insert(0,7)

my_array.extend([5,8,0])

my_array.fromlist([1,2,3,4,5])

my_array.remove(1)

my_array.pop() # removes the last element 

my_array.index(1)

my_array.reverse() # reverse

my_array.buffer_info() #

my_array.count(1) # count # of occurances of the element

my_array.tolist()

my_array[1:6]


# Two Dimemensional Array

import numpy as np

twodarray = np.array([[1,2,3],[4,5,6]])

twodarray

# to insert a column in my array with 2 rows and at position of 0

np.insert(twodarray,0,[7,8], axis=1)

np.insert(twodarray,2,[9,10,11], axis=0)

# carefully notice the below statements 

np.append(twodarray,[[12,13,14]], axis=0)
np.append(twodarray,[[12],[13]], axis=1)



