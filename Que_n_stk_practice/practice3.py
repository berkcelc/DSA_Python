"""
To implement a set of sub stacks that has similar property as of the stack and
one the last stack is filled, it automaticall creates a new substack
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        c_node = self.head
        while c_node:
            yield c_node
            c_node = c_node.next



class MasterStack:
    def __init__(self, size):
        self.linkedlist = LinkedList()
        self.n_substack = 0
        self.stack_size = size
        self.count_element = 0

    def __str__(self):
        vals = [str(x.value) for x in self.linkedlist]
        return vals.reverse()


    def push(self, value):
        new_node = Node(value)
        if self.count_element % self.stack_size == 0:
            self.n_substack += 1
        self.count_element += 1
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
        else:
            new_node.next = self.linkedlist.head
            self.linkedlist.head = new_node

    def pop(self):
        if self.linkedlist.head == None:
            return "the stack is empty"
        else:
            self.count_element -= 1
            if self.count_element % self.stack_size == 0:
                self.n_substack = self.count_element // self.stack_size
            else:
                self.n_substack = (self.count_element // self.stack_size) + 1
            val = self.linkedlist.head
            self.linkedlist.head = self.linkedlist.head.next
            return val.value
        
    def popat(self, index):
        if index > self.n_substack:
            return "The address does not reside in the location"
        else:
            position = ((index-1) * self.stack_size) + 1
            print(position)
            # we will move to the position 
            pointer = self.linkedlist.head
            for _ in range(position - 2):
                pointer = pointer.next
            val = pointer.next
            
            pointer = pointer.next.next
            return val.value


ms = MasterStack(3)
ms.push(1)
ms.push(2)
ms.push(3)
ms.push(4)

ms.pop()

ms.n_substack

ms.popat(2)