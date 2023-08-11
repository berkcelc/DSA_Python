from Linked_List_Interview_Questions.practice1 import *

cll = LinkedList()

cll.generate(12,0,100)

print(cll)

cll.head.next.value

def kth_element_from_end(ll,k):
    element_set = []
    c_node = ll.head    
    while c_node.next is not None:
        element_set.append(c_node.value)
        c_node = c_node.next
    return element_set[-k+1]

kth_element_from_end(cll,2)