# creating a Node class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


new_node = Node(10)


print(new_node)

# Time complexity O(1) --- for creating 1 node object
# Space complexity O(1)

# Linked List constructor

class LinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0

new_linked_list = LinkedList(10)
print(new_linked_list.head)

# creation of linked List
# Time complexity O(1) --- for creating 1 node object
# Space complexity O(1) --- for creating 1 node object


# Insertion in sll

# There are three steps to add a node to a linked list\

# 1. create a new Node
# 2. set the new node's value
# 3. Update the node's address




