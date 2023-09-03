

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


newbt = TreeNode('Drinks')
leftchild = TreeNode('Hot')
leftchild1 = TreeNode('Cola')
leftchild2 = TreeNode('Fanta')
rightchild = TreeNode('Cold')
rightchild1 = TreeNode('Tea')
rightchild2 = TreeNode('Coffee')



newbt.leftchild = leftchild
newbt.rightchild = rightchild

rightchild.rightchild = leftchild1
rightchild.leftchild = leftchild2

leftchild.leftchild = rightchild1
leftchild.rightchild = rightchild2

# creating an insert function in the root node
def insert_node(rootnode, value):
    newnode = TreeNode(value)
    if not rootnode:
        rootnode = newnode
        return "The node has been inserted"
    else:
        temp_list = []
        temp_list.append(rootnode)
        while len(temp_list) > 0:
            _ret = temp_list.pop(0)
            
            if _ret.leftchild is not None:
                temp_list.append(_ret.leftchild)
            else:
                _ret.leftchild = newnode
                return "The node has been inserted"
            
            if _ret.rightchild is not None:
                temp_list.append(_ret.rightchild)
            else:
                _ret.rightchild = newnode
                return "The node has been inserted"
            

insert_node(newbt,'chai')

