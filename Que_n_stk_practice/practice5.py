# implementing a queue for animal shelter

class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, animal):
        self.list.append(animal)
        return 'The animal has been successfully added'
    
    def dequeue_dog(self):
        # find the first dog
        for i,n in enumerate(self.list):
            if n == 'dog':
                return self.list.pop(i)
        return "No dogs are left"

    def dequeue_cat(self):
        # find the first dog
        for i,n in enumerate(self.list):
            if n == 'cat':
                return self.list.pop(i)
        return "No cats are left"
    
    def dequeue_any(self):
        if len(self.list) > 0:
            return self.list.pop(0)
        else:
            return "No animal in the shelter"
    

    
q = Queue()

q.enqueue('cat')
q.enqueue('cat')
q.enqueue('cat')
q.enqueue('dog')
q.enqueue('cat')
q.enqueue('cat')
q.dequeue_dog()


