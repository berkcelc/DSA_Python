"""
Check the intersection of the elements between two nodes

"""

from Linked_List_Interview_Questions.practice1 import *

cll1 = LinkedList()
cll2 = LinkedList()

cll1.generate(7,0,10)
cll2.generate(7,0,10)


print(cll1)
print(cll2)

def check_intersection(ll1, ll2):
    c_node1 = ll1.head
    c_node2 = ll2.head
    common_elements = []
    while c_node1:
        if c_node1.value == c_node2.value:
            common_elements.append(c_node1.value)
        c_node1 = c_node1.next
        c_node2 = c_node2.next
    return common_elements

check_intersection(cll1, cll2)



"""
Now we need to check intersection by node, the Linked Lists should have the same node
"""

def check_interesection_node(ll1, ll2):

    # Time complexity ---> O (A + B)

    if ll1.tail is not ll2.tail:
        return False
    lenA = len(ll1)
    lenB = len(ll2)
    shorter = ll1 if lenA < lenB else ll2
    longer = ll2 if lenA < lenB else ll1

    diff = len(longer) - len(shorter)

    # print(diff)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.head

    while shorterNode is not longerNode:
        print(shorterNode.value)
        shorterNode =  shorterNode.next
        longerNode = longerNode.next

    return longerNode


"""
to have linked list that has same node we need a 
function that will add the same node to the 
"""
def add_node(ll1, ll2, value):
    temp_node = Node(value)
    ll1.tail.next = temp_node
    ll1.tail = temp_node
    ll2.tail.next =temp_node
    ll2.tail = temp_node


add_node(cll1, cll2, 7)
add_node(cll1, cll2, 3)
add_node(cll1, cll2, 4)


print(cll1) 
print(cll2)

print(check_interesection_node(cll1, cll2))


