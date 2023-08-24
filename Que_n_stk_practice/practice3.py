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

class MasterStack:
    def __init__(self, size):
        self.linkedlist = LinkedList()
        self.n_substack = 0
        self.stack_size = size
        self.count_element = 0

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


