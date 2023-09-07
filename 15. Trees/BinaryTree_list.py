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

    def inordertraversal(self, index):
        if index > self.lastusedindex:
            return
        self.inordertraversal(index * 2)
        print(self.customlist[index])
        self.inordertraversal(index * 2 + 1)

    def postordertraversal(self, index):
        if index > self.lastusedindex:
            return
        self.postordertraversal(index * 2)
        self.postordertraversal(index * 2 + 1)
        print(self.customlist[index])

    def levelordertraversal(self, index):
        if index > self.lastusedindex:
            return
        for i in range(index, self.lastusedindex + 1):
            print(self.customlist[i])

    def deletenode(self, value):
        if self.lastusedindex == 0:
            return "There are no elements to delete"
        for i in range(1, self.lastusedindex):
            if self.customlist[i] == value:
                self.customlist[i] = self.customlist[self.lastusedindex]
                self.customlist[self.lastusedindex] = None
                self.lastusedindex =- 1
                return "The element has been deleted"
                
    def deleteall(self):
        self.customlist = None
        return "The binary tree has been deleted"


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

newbt.preordertraversal(1)
newbt.inordertraversal(1)
newbt.postordertraversal(1)
newbt.levelordertraversal(1)