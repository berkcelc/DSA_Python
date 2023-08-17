"""
The new elements are pushed to the head of the linked list
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

class Stack:
    def __init__(self):
        self.LinkedLlist = LinkedList()

    def __str__(self):
        """ 
        A very important observation :- The list method reverse() will change the list and reverse the elements 
        So it is important to use with  caution
        """
        values = [str(x.value) for x in self.LinkedLlist]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedLlist.head is None:
            return True
        else:
            return False
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.LinkedLlist.head
        self.LinkedLlist.head = new_node

    def pop(self):
        if self.isEmpty():
            return "There is no element"
        else:
            c_node = self.LinkedLlist.head
            self.head = self.LinkedLlist.head.next
            c_node.next = None
            return c_node.value


stk = Stack()

stk.push(10)
stk.push(9)
stk.pop()
print(stk)
