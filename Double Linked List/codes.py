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


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # go to the last element  and add a element
            self.tail.next = new_node
            new_node.prev= self.tail
            self.tail = new_node

    def add_node(self, value, position):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            if position == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            elif position == -1:
                self.tail.next = new_node
                new_node.prev= self.tail
                self.tail = new_node

            else:
                c_node = self.head
                for _ in range(position - 1):
                    c_node = c_node.next
                c_node.next.prev = new_node
                new_node.next = c_node.next
                c_node.next = new_node
                new_node.prev = c_node

    # method to traverse through the linked list
    def traverse(self):
        c_node = self.head
        while c_node:
            print(c_node.value)
            c_node = c_node.next

    #searching through the linked list
    def search_element(self, element):
        c_node = self.head
        while c_node:
            if c_node.value == element:
                print("The element exists")
                break
            c_node = c_node.next
        else:
            print("The element does not exists")

    
    def delete_element(self, position):
        if self.head is None:
            return "The linked list is empty"
        
        else:
            if position == 0:
                new_head = self.head.next
                self.head.next = None
                new_head.prev = None
                self.head = new_head
            elif position == -1:
                new_tail = self.tail.prev
                new_tail.next = None
                self.tail.prev = None
                self.tail = new_tail
            else:
                c_node = self.head
                for _ in range(position-1):
                    c_node = c_node.next
                delete_node = c_node.next
                delete_node.next.prev = c_node
                c_node.next = delete_node.next
                delete_node.next = None
                delete_node.prev = None

    def delete_all(self):
        self.head = None
        self.tail = None


    def reverse(self):

        c_node = self.head
        self.tail = self.head
        while c_node:
            
            """
            I was facing a decent amount of challange here as 
            at the tail, I was setting the head to None which was the step in the last one,
            Needed to insert an if statement to change the narrative
            """
            if c_node.next is None:
                self.head = c_node
            
            next = c_node.next
            c_node.next = c_node.prev
            c_node.prev = next
            c_node = next
            print(next)
            
        # self.head = c_node
        # print(c_node.value, self.tail.value)




dll = DoubleLinkedList()
dll.create(2)
dll.append(0)
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.add_node(7,3)
dll.traverse()
dll.search_element(3)
# dll.delete_element(2)
# dll.delete_all()

[node.value for node in dll]

dll.reverse()

