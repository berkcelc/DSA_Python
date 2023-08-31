"""
Here are the common operation that we can perform 
on the binary tree using linked List

1. Creation of Tree
2. Insertion of a node
3. Deletion of a node
4. Searching of a node
5. Traverse all the nodes
6. Deletion of tree
"""

from typing import Any


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


bt = TreeNode('Drinks')
        