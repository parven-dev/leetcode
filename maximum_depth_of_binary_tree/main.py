# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.right)
        right = self.maxDepth(root.left)

        return max(left, right) + 1
        




