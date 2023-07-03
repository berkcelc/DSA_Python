

eng_sp = dict(one='uno', two='dos', three='tres')

eng_sp2 = {'one':'uno', 'two':'dos', 'three':'tres'}


_ = eng_sp2.pop('one')

_

eng_sp2.popitem()


my_dict = {'five':4, 'five':5}
my_dict

# some methods for the dictionary

my_dict.copy() # creates a new copy of the dictionary



my_dict.fromkeys() # creates a new dictionary

{}.fromkeys([1,2,3]) # creates a new dictionary

my_dict.clear()

eng_sp.get('one1')

eng_sp.items()

eng_sp.keys()

# popitem() does not take any input and returns an arbitrary element from the dictionary


# setdefault()

eng_sp.setdefault('three', 3) # sets

eng_sp.update({'five':4, 'five':5})

eng_sp


# python functions to work with the dictionaries

4 in eng_sp.values() # returns

all(eng_sp)

sorted(eng_sp)
eng_sp

stocks = ['abb','infy','infoltd','tcs','reliance']

s_d = {}

n = {x:'NSE' for x in stocks}

n_d = {new_k.capitalize():new_v for (new_k,new_v) in n.items() if len(new_k) == 3 }

n_d

# merging two dictionaries with addition in case the value exists in the first one

def merge(dict1, dict2):
    new_dict = dict1.copy()
    for key, values in dict2.items():
        new_dict[key] = new_dict.get(key, 0) + values
    return new_dict


# Time Complexity - O(n + m)
# Space Complexity - O(m + n)

# getting the key that holds the maximum value

my_dict = {'one':1, 'two':2, 'three':3}
max(my_dict, key=my_dict.get)



def check_same_frequency(list1, list2):
    d1 = {}
    d2 = {}
    for i in list1:
        d1[i] = d1.get(i,0) + 1
    print(d1)
    for i in list2:
        d2[i] = d2.get(i,0) + 1
    print(d2)
    return d1 == d2

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)


