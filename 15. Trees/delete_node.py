
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


def delete_deepest_node(rootnode):
    dnode = get_deepest_node(newbt)
    if not rootnode:
        return
    else:
        _temp = []
        _temp.append(rootnode)
        while len(_temp) > 0:
            _ret = _temp.pop(0)
            if _ret.data == dnode:
                _ret = None
            if _ret.rightchild:
                if _ret.rightchild.data == dnode:
                    _ret.rightchild = None
                    return
                else:
                    _temp.append(_ret.rightchild)
                
            if _ret.leftchild:
                if _ret.leftchild.data == dnode:
                    _ret.leftchild = None
                    return
                else:
                    _temp.append(_ret.leftchild)
                


def delete_node(rootnode, node):
    if not rootnode:
        return 
    else:
        _temp = []
        _temp.append(rootnode)

        while len(_temp) > 0:
            _ret = _temp.pop(0)
            if _ret.data == node:
                dnode = get_deepest_node(rootnode)
                print(dnode)
                delete_deepest_node(rootnode=rootnode)
                _ret.data = dnode
                return "The link has been successfully deleted"
            if (_ret.leftchild) is not None:
                _temp.append(_ret.leftchild)
            if _ret.rightchild is not None:
                _temp.append(_ret.rightchild)
        return "Failed to delete"

delete_node(newbt, 'Hot')