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


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# updating the __str__ to fulfill our requirements.
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def add_node(self, value, location):
        new_node = Node(value)


        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        elif location == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            temp_loc = self.head
            for _ in range(location - 1):
                temp_loc = temp_loc.next
            new_node.next = temp_loc.next
            temp_loc.next = new_node
        self.length += 1
                
    def traverse(self):
        temp_loc = self.head
        while temp_loc:
            print(temp_loc.value)
            temp_loc = temp_loc.next

    def delete(self, location):
        temp_loc = self.head
        for i in range(location - 2):
            temp_loc = temp_loc.next
        temp_loc.next = temp_loc.next.next.next
        temp_loc.next.next = None
        self.length -= 1

    def search(self, value):
        temp_loc = self.head
        index = 0
        while temp_loc:
            if value == temp_loc.value:
                print("Found")
                return index 
            temp_loc = temp_loc.next
            index += 1

    def get(self, index):
        temp_loc = self.head
        for _ in range(index):
            temp_loc = temp_loc.next
        return temp_loc
    
    def set(self, index, value):
        temp = self.get(index)
        temp.value = value        


    def pop_first(self):
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        popped.next = None
        return popped
    
    def pop(self):
        popped = self.tail
        temp = self.head

        while temp.next is not self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.length -= 1
        return popped
    
    def remove(self, index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    

    

sample_linked_list = LinkedList()
sample_linked_list.append(10)
sample_linked_list.append(20)
sample_linked_list.prepend(30)
sample_linked_list.__str__()
# Inserting an element into a linked list
sample_linked_list.add_node(40, 2)
sample_linked_list.traverse()
sample_linked_list.delete(2)
sample_linked_list.search(10)

sample_linked_list.set(2, 100)