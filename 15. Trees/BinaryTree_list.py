class BinayTree:
    def __init__(self, size):
        self.customlist = size * [None]
        self.lastusedindex = 0
        self.maxsize = size

    def insertnode(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return "The binary tree is full"
        else:
            self.customlist[self.lastusedindex + 1] == value
            self.lastusedindex += 1
            return "The value has been successfully inserted"
        
    def searchnode(self, value):
        for i in range(self.customlist):
            if self.customlist[i] == value:
                return "Success"
        return "Not Found"

newbt = BinayTree(10)
        