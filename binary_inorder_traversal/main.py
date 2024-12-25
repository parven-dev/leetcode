# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        data = []
        self.Traversal(root, data)
        return data

    def Traversal(self, root, data):
        if not root:
            return None
        self.Traversal(root.left, data)
        data.append(root.val)
        self.Traversal(root.right, data)
