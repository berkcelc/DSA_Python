from Linked_List_Interview_Questions.practice1 import *

cll = LinkedList()

cll.generate(12,0,10)

print(cll)


# remove duplicates

def remove_dupes(ll):
    """
    Removes duplicate elements from a given linked list.
    
    Parameters:
        ll (LinkedList): The linked list to remove duplicates from.
        
    Returns:
        LinkedList: The linked list with duplicate elements removed.
        
    Raises:
        None
    """
    if ll.head is None:
        return "There is no element in this Linked List"
    else:
        elements = []
        c_node = ll.head
        elements.append(c_node.value) # append the first element
        while c_node.next is not None: # loop through the linked list
            if c_node.next.value in elements: # check if the element is in the list
                c_node.next = c_node.next.next # if it is remove it
                continue                        # and continue the loop from start without appending any value further
            elements.append(c_node.next.value) # append the next element if the element is not in the list
            c_node = c_node.next # go to the next element if the element is not in the list
    return ll


l1 = remove_dupes(cll)
print(l1)



