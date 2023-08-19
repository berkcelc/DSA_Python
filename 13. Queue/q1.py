class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values) 

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, values):
        self.items.append(values)
        return "The item is inserted"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            return self.items.pop(0)
    def delete(self):
        self.items = None    
    
        