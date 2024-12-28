# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        data = []
        self.InOrderTraversal(root, data)
        return len(data)

    def InOrderTraversal(self,root, data):
        if not root:
            return None
        self.InOrderTraversal(root.left, data)
        data.append(root.val)
        self.InOrderTraversal(root.right, data)
        
