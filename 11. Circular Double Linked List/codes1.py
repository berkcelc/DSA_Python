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

            elif location == -1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node

            else:
                temp_node = self.head
                for _ in range(location - 1):
                    temp_node = temp_node.next
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node

            # return "The node has been successfully inserted"
        

    def traverse(self):
        if self.head is None:
            return "There is no node for traversal"
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                if tempnode == self.tail:
                    break
                tempnode = tempnode.next


    def search(self,value):
        if self.head is None:
            return "There is no element in this list"
        else:
            c_node  = self.head
            while c_node:
                if c_node.value == value:
                    return " the value exists in the list"
                if c_node.next == self.head:
                    return "the value does not exists"


    def reversetraverse(self):
        if self.head is None:
            print("There is not any node for reverse traversal")
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                if tempnode == self.head:
                    break
                tempnode =tempnode.prev

                

cdll = CircularDoublyLinkedList()

cdll.create(5)
cdll.insert(7,0)
cdll.insert(6,-1)
cdll.insert(5,1)


[node.value for node in cdll]

cdll.traverse()


cdll.search(6)