class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
 
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):

        # This function is for printing the values of the linked list

        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next


    # creating a node
    def create(self, value):
        node = Node(value)
        node.next = node    
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
circulrSLL = CircularSinglyLinkedList()
circulrSLL.create(1)


# for this reason we used the Iter tool
[node.value for node in circulrSLL]
