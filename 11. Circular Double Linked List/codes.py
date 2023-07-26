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
            node = node.next
            if node == self.tail.next:
                break

    def create(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        
    
    def insert(self, value, location):
        new_node = Node(value)
        if self.head is None:
            return "The cdll does not exists"
        

        else:
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.head = new_node

            if location == -1:
                self.tail.next = new_node
                self.head.prev = new_node
                new_node.prev = self.tail
                self.tail = new_node

            else:
                c_node = self.head
                for _ in range(location - 1):
                    c_node = c_node.next
                c_node.next.prev = new_node
                new_node.next = c_node.next
                new_node.prev = c_node
                c_node.next = new_node

    def traverse(self):
        c_node = self.head
        while c_node:
            print(c_node.value)
            c_node = c_node.next
            if c_node == self.head:
                break

            # return "The node has been successfully inserted"
        

cdll = CircularDoublyLinkedList()

cdll.create(5)
cdll.insert(7,0)
# cdll.insert(6,-1)
cdll.insert(5,1)


[node.value for node in cdll]



