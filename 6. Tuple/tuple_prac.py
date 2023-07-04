

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


# element wise addition

t1 = 1,2,3
t2 = 4,5,6


t1 + t2


# there are 2 ways to do element wise operation for given two tuple

tuple(a + b for (a, b) in zip(t1, t2)) # we need to write the tuple statement
tuple(map(sum, zip(t1, t2)))

('Hello', 'world')


def concatenate_strings(input_tuple):
    text = input_tuple[0]
    print(text)
    for i in range(1, len(input_tuple)):
        print(input_tuple[i])
        text = text + ' ' + input_tuple[i]
    return text
    

concatenate_strings(('Hello', 'world'))

# a very short version
' '.join(('Hello', 'world'))

len(t1)

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

# to get the common elements between two tuples
# tuple(set(tuple1) & set(tuple2))

