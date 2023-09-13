
"""
There are two ways of implementing Binary heap
1. Arrays
2. Reference / Pointer Implementation
"""

class Heap:
    def __init__(self, size):
        self.customlist = [None] * (size + 1)
        self.heapsize = 0
        self.maxsize = size + 1

def peekofheap(rootnode):
    if not rootnode:
        return 
    else:
        return rootnode.customlist[1]
    
# size of heap is the number of elements in the heap

def sizeofheap(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.heapsize
    
def levelordertraversal(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1, rootnode.heapsize +1):
            print(rootnode.customlist[i])

            
def heapifytreinsert(rootnode, index, heaptype):
    parentindex = int(index/2)
    if index <= 1:
        return
    if heaptype == "min":
        if rootnode.customlist[index] < rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
        heapifytreinsert(rootnode, parentindex, heaptype)

    elif heaptype == 'Max':
        if rootnode.customlist[index] > rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
        heapifytreinsert(rootnode, parentindex, heaptype)


def insertnode(rootnode, nodevalue, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
        return "The binary heap is full"
    rootnode.customlist[rootnode.heapsize + 1]  = nodevalue
    rootnode.heapsize += 1
    heapifytreinsert(rootnode, rootnode.heapsize, heaptype)
    return "the value has been successfully inserted"




def heapifytreeextract(rootnode, index, heaptype):
    leftindex = index * 2
    rightindex = index *2 + 1
    swapchild = 0

    if rootnode.heapsize < leftindex:
        return 
    elif rootnode.heapsize == leftindex:
        if heaptype == 'Min':
            if rootnode.customlist[index] > rootnode.customlist[leftindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return 
        elif heaptype == 'Max':
            if rootnode.customlist[index] < rootnode.customlist[leftindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return


    else:
        if heaptype == 'Min':
            if rootnode.customlist[leftindex] < rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if rootnode.customlist[index] > rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp

        else:
            if rootnode.customlist[leftindex] > rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if rootnode.customlist[index] > rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp

    heapifytreeextract(rootnode, swapchild, heaptype)

def extractnode(rootnode, heaptype):
    if rootnode.heapsize == 0:
        return
    else:
        extractednode = rootnode.customlist[1]
        rootnode.customlist[1] = rootnode.customlist[rootnode.heapsize]
        rootnode.customlist[rootnode.heapsize] = None
        rootnode.heapsize -=1
        heapifytreeextract(rootnode,1,heaptype)
        return extractednode
    











newheap = Heap(5)

insertnode(newheap, 4,"Max")
insertnode(newheap, 3,"Max")
insertnode(newheap, 4,"Max")
insertnode(newheap, 5,"Max")
insertnode(newheap, 10,"Max")


levelordertraversal(newheap)


