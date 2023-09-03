
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


def get_deepest_node(rootnode):
    if not rootnode:
        return 
    else:
        _temp = []
        _temp.append(rootnode)
        while len(_temp) > 0:
            _ret = _temp.pop(0)

            if _ret.leftchild is not None:
                _temp.append(_ret.leftchild)
            if _ret.rightchild is not None:
                _temp.append(_ret.rightchild)
        return _ret.data
            

get_deepest_node(newbt)


def delete_deepest_node(rootnode, dnode):
    if not rootnode:
        return
    else:
        _temp = []
        _temp.append(rootnode)
        


