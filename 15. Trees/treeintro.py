class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=9):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    def addchild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks',[])

cold = TreeNode('Cold',[])

hot = TreeNode('Hot', [])

tree.addchild(cold)
tree.addchild(hot)
print(tree)
