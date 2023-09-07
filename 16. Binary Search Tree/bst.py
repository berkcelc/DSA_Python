"""
These are the operation that we can perform on bst
1. creation of tree
2. Insertiom of node
3. Deletion of a node
4. search for a node
5. Traverse of node
6. Deletion of a tree
"""

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def insertnode(rootnode, nodevalue):
    if rootnode.data == None:
        rootnode.data = nodevalue
    elif nodevalue <= rootnode.data:
        if rootnode.leftchild == None:
            rootnode.leftchild = BSTNode(nodevalue)
        else:
            insertnode(rootnode.leftchild, nodevalue)
    else:
        if rootnode.rightchild == None:
            rootnode.rightchild = BSTNode(nodevalue)
        else:
            insertnode(rootnode.rightchild, nodevalue)


# traversal is similar to the one in Binarytree
# pre - in - post - level 

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
    


newbst = BSTNode(None)

insertnode(newbst,70)
insertnode(newbst,90)
insertnode(newbst,80)

