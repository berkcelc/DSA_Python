class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):

        """ 
        A very important observation :- The list method reverse() will change the list and reverse the elements 
        So it is important to use with  caution
        """

        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    

    # check if the stack is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # push a value to the stack
    def push(self,a):
        self.list.append(a)
        return "The element is added"
    
    # pop method from the list
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            print(self.list)
            return self.list.pop()
    # peek -- > to return the last element of the stack

    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[-1]
        
    def delete(self):
        self.list = None
        return "The stack has been deleted"

        
r_s = Stack()


print(r_s.isEmpty())

r_s.push(1)
r_s.list
r_s.push(2)
r_s.list
r_s.push(3)
r_s.list
r_s.push(4)
r_s.list

print(r_s)
r_s.pop()
r_s.peek()
