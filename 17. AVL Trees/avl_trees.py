class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1


def preordertraversal(rootnode):
    if rootnode is None:
        return 
    print(rootnode.data)
    preordertraversal(rootnode.leftchild)
    preordertraversal(rootnode.rightchild)


def inordertraversal(rootnode):
    if rootnode is None:
        return 
    inordertraversal(rootnode.leftchild)
    print(rootnode.data)
    inordertraversal(rootnode.rightchild)

def postordertraversal(rootnode):
    if rootnode is None:
        return 
    postordertraversal(rootnode.leftchild)
    postordertraversal(rootnode.rightchild)
    print(rootnode.data)



def levelordertraversal(rootnode):
    if not rootnode:
        return
    else:
        temp_list = []
        temp_list.append(rootnode)
        while len(temp_list) > 0:
            _ret = temp_list.pop(0)
            print(_ret.data)
            if _ret.leftchild is not None:
                temp_list.append(_ret.leftchild)
            if _ret.rightchild is not None:
                temp_list.append(_ret.rightchild)


def searchnode(rootnode, nodevalue):
    if rootnode.data == nodevalue:
        print("The value is found")
    elif nodevalue < rootnode.data:
        if rootnode.leftchild.data == nodevalue:
            return "the value is found"
        else:
            searchnode(rootnode.leftchild, nodevalue)
    else:
        if rootnode.rightchild.data == nodevalue:
            return "The value is found"
        else:
            searchnode(rootnode.rightchild, nodevalue)
    

# Inserting a node in avl tree

# first we will be creating some helper functions 

def getheight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def rightrotate(disbalancedNode):
    newroot = disbalancedNode.leftchild
    disbalancedNode.leftchild = newroot.rigtchild
    newroot.rightchild = disbalancedNode
    disbalancedNode.height = 1 + max(getheight(disbalancedNode.leftchild), getheight(disbalancedNode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot

def leftrotate(disbalancedNode):
    newroot = disbalancedNode.rightchild
    disbalancedNode.rightchild = newroot.leftchild
    newroot.leftchild = disbalancedNode
    disbalancedNode.height = 1 + max(getheight(disbalancedNode.leftchild), getheight(disbalancedNode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot

def getbalance(rootnode):
    if not rootnode:
        return 0
    return getheight(rootnode.leftchild) - getheight(rootnode.rightchild)


def insertnode(rootnode, value):
    if not rootnode:
        return AVLNode(value)
    elif value < rootnode.data:
        rootnode.leftchild = insertnode(rootnode.leftchild, value)
    else:
        rootnode.rightchild = insertnode(rootnode.rightchild, value)
    rootnode.height  = 1 + max(getheight(rootnode.leftchild), getheight(rootnode.rightchild))
    balance = getbalance(rootnode)






