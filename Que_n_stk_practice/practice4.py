"""
Implement a queue using two stacks.
"""

class Node:
    def __init__(self, value = None):
        self.value  = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self) -> None:
        self.linkedlist = Linkedlist()

    def add()