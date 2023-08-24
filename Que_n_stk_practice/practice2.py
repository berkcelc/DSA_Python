"""
To implement a stack with a min method that returns the min of the stack
push, pop and min should all be with time comlpexity O(1)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()
        self.minlist = LinkedList()

    def get_min(self):
        if self.minlist.head is None:
            return "The stack is empty"
        else:

            return self.minlist.head.value

    def push(self, value):
        new_node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
            self.minlist.head = new_node
            self.minlist.tail = new_node
        else:
            new_node.next = self.linkedlist.head
            self.linkedlist.head = new_node
            if new_node.value < self.minlist.head.value:
                new_node.next = self.minlist.head
                self.minlist.head = new_node
            else:
                _t_node = Node(self.minlist.head.value)
                _t_node.next = self.minlist.head
                self.minlist.head = _t_node



    def pop(self):
        if self.linkedlist.head is None:
            return "There is no element in the stack"
        else:
            value = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            self.minlist.head = self.minlist.head.next
            return value
        


stk = Stack()

stk.push(20)
stk.push(15)
stk.push(17)
stk.push(8)
stk.push(3)
stk.push(2)

stk.get_min()
stk.pop()
