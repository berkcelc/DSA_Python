class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        c_node = self.head
        while c_node:
            yield c_node
            c_node = c_node.next

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        vals = [str(x) for x in self.linkedlist]
        return ' '.join(vals)
    


    def enqueue(self, value):
        self.linkedlist.add(value)
        return "The element has been successfully inserted"
    
    def dequeue(self):
        pass

    

