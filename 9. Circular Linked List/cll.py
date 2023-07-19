class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
 
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):

        # This function is for printing the values of the linked list

        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next


    # creating a node
    def create(self, value):
        node = Node(value)
        node.next = node    
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
    # adding an element to the csll
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            return "The CSLL has been created"
            
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        # self.length += 1

    def add_at_start(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node


    def add_at_position(self,position, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head

        elif position == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        # what if the position is the last element
        elif position == -1:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        else:
            pos_node = self.head
            for _ in range(position - 1):
                pos_node = pos_node.next
            
            new_node.next = pos_node.next
            pos_node.next = new_node



    def traverse(self):
        if self.head is None:
            print("The CSLL is empty")
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    break


    def search_element(self, number):
        print(number)
        if self.head is None:
            print("The csll is empty") 
        else:
            temp_ = self.head
            
            while temp_:
                if temp_.value == number:
                    return "The value exists"
                temp_ = temp_.next
                if temp_ == self.tail.next:
                    return "The value does not exist"
                

    # we will add the delete methods here itself

    def deletenode(self, location):

        if self.head is None:
            print("There is no element in this csll")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.tail = None
                    self.head = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            if location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    c_node = self.head
                    while c_node.next != self.tail:
                        c_node = c_node.next
                    self.tail = c_node
                    c_node.next = self.head

            else:
                c_node = self.head
                for i in range(location - 1):
                    c_node = c_node.next
                c_node.next = c_node.next.next

    def deleteall(self):
        self.head = None
        self.tail.next = None
        self.tail = None




                



circulrSLL = CircularSinglyLinkedList()

circulrSLL.add_at_position(0, 14)

circulrSLL.create(1)

circulrSLL.append(2)
circulrSLL.append(3)
circulrSLL.append(4)
circulrSLL.append(5)


circulrSLL.add_at_start(0)



# for this reason we used the Iter tool
[node.value for node in circulrSLL]

circulrSLL.traverse()

circulrSLL.search_element(4)


circulrSLL.deletenode(2)


circulrSLL.deleteall()

