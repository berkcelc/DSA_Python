# creating a node for double linked list

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # iterating over the linked list

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # creating a node

    def create(self, value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node
        

dll = DoubleLinkedList()

dll.create(2)

[node.value for node in dll]
