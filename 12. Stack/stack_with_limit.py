class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    
    def __str__(self):

        """ 
        A very important observation :- The list method reverse() will change the list and reverse the elements 
        So it is important to use with  caution
        """

        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def iffull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
        
    def push(self, value):
        if self.iffull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The value has been inserted"
        