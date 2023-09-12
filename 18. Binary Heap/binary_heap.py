
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

            
        

