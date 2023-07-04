

t1 = 1,2,'d'  # we dont need the brackets to declare a tuple
t1
t2 = (4,5,6)

for i in t1:
    print(i)


1 in t1

t1 + t2 # concatenate

t1 * 10 # creates a new tuple

t2.count(7) # returns the count of the element
t2.index(4) # returns the index of the element

max(t2) # returns the maximum
min(t2) # returns the minimum


# Time complexity of creating a tuple is  O(1)

