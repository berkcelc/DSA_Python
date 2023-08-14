"""A number is represented by linked List in such a way that the last digit is at head and the first is at tail
Add two linked list numbers and give the output in form of a linkedlist

"""



from Linked_List_Interview_Questions.practice1 import *

cll1 = LinkedList()
cll2 = LinkedList()

cll1.generate(3,0,10)
cll2.generate(3,0,10)

print(cll2)


def add_ll(ll1, ll2):
    new_ll = LinkedList()
    c_node1 = ll1.head
    c_node2 = ll2.head
    carry = 0
    while c_node1:
        digit = c_node1.value + c_node2.value + carry
        carry = digit // 10
        rem = digit % 10
        new_ll.add(int(rem))
        c_node1 = c_node1.next
        c_node2 = c_node2.next
    if carry != 0:
        new_ll.add(carry)
    return new_ll

print(cll1)
print(cll2)
print(add_ll(cll1, cll2))


