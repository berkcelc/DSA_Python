from practice1 import *

cll = LinkedList()

cll.generate(12,0,10)

print(cll)


# remove duplicates

def remove_dupes(ll):
    if ll.head is None:
        return "There is no element in this Linked List"

    else:
        elements = []
        elements.append(ll.head.value)
        c_node = ll.head
        while c_node.next is not None:
            elements.append(c_node.value)
            if c_node.next.value in elements:
                
                if c_node.next == ll.tail:
                    ll.tail = c_node
                    c_node.next = None
                else:
                    c_node.next = c_node.next.next
            c_node = c_node.next

    return ll


l1 = remove_dupes(cll)
print(l1)



