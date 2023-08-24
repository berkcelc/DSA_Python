
class Multistack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.stacksize = stacksize
        self.list = [0] * (self.stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks

    def isfull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
        
    def isempty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
        
    def indexoftop(self, stacknum):
        return self.stacksize * (stacknum) + (self.sizes[stacknum]) - 1
    
    def push(self, item, stacknum):
        if self.isfull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.list[self.indexoftop(stacknum)] = item

    def pop(self, stacknum):
        if self.isempty(stacknum):
            return "there is no element in the stack"
        else:
            value = self.list[self.indexoftop(stacknum)]
            self.list[self.indexoftop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
        


