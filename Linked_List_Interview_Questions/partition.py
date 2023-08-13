"""
write a function that rearranges a linked list such that all the elements that 
are less fall on one side and all the elements that are greater fall on the other side

"""

from Linked_List_Interview_Questions.practice1 import *

cll = LinkedList()

cll.generate(12,0,100)

print(cll)


def partition_ll(ll,part):
    # creating a new linked list
    rll = LinkedList()
    rll.add(ll.head.value)
    c_node = ll.head.next

    while c_node:
        if c_node.value >= part:
            rll.add(c_node.value)
        else:
            rll.preadd(c_node.value)
        c_node = c_node.next

    return rll

new_ll = partition_ll(cll, 50)

print(new_ll)


# without creating a new Linked List 

def partition2(ll, part):
    c_node = ll.head
    ll.tail = ll.head

    while c_node:
        next_node = c_node.next
        c_node.next = None
        if c_node.value < part:
            c_node.next = ll.head
            ll.head = c_node
        else:
            ll.tail.next = c_node
            ll.tail = c_node
        c_node = next_node

    if ll.tail.next is not None:
        ll.tail.next = None
