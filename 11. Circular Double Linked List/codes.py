# creating a node for double linked list

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def create(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node



cdll = CircularDoublyLinkedList()

cdll.create(5)

[node.value for node in cdll]