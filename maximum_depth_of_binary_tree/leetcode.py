# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inOrderTraversal(self, root,):
       result = []
       self.Traversal(root, result)
       return result

    def Traversal(self, root, result):
        if not root:
            return None
        self.Traversal(root.left, result)
        result.append(root.val)
        self.Traversal(root.right, result)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_value = float("inf")

        result = self.inOrderTraversal(root)

        for item in range(len(result)-1):
            my_data = result[item + 1] - result[item]
            if my_data < min_value:
                min_value = my_data

        return min_value



        