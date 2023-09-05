class BinayTree:
    def __init__(self, size):
        self.customlist = size * [None]
        self.lastusedindex = 0
        self.maxsize = size

    def insertnode(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return "The binary tree is full"
    
        print(value, self.lastusedindex)
        self.customlist[self.lastusedindex + 1] = value
        self.lastusedindex += 1
        return "The value has been successfully inserted"
    
    def searchnode(self, value):
        for i in range(self.maxsize):
            if self.customlist[i] == value:
                return "Success"
        return "Not Found"
    
    def preordertraversal(self, index):
        if index > self.lastusedindex:
            return
        print(self.customlist[index])
        self.preordertraversal(index*2)
        self.preordertraversal(index*2 + 1)

# there is some issue with preorder traversal, debug it 


newbt = BinayTree(10)
newbt.insertnode('Drinks')     
newbt.insertnode('Hot')     
newbt.insertnode('Cold')     
newbt.insertnode('Tea')     
newbt.insertnode('Coffee')     
newbt.insertnode('Cola')     
newbt.insertnode('Fanta')

newbt.customlist

newbt.searchnode('Fanta')

newbt.preordertraversal(0)
