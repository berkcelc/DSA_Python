class Queue:
    def __init__(self, maxsize):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values) 
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return "The queue is Full"
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted in the queue"
        
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            val = self.items[self.start]
            self.items[self.start] = None
            if self.start == self.top:
                self.start = self.top = -1
            elif self.start + 1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1
            return val
        
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items = self.maxsize * [None]
        self.start = self.top = -1

        

q = Queue(3)
    
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)

q.enqueue(1)
q.dequeue()

q.isFull()
 
q.peek()

