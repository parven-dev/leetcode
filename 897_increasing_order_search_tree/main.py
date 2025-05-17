
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        dummy_node = TreeNode(0)
        self.current = dummy_node
        
        def inOrder(node):
            if not node:
                return 
            
            inOrder(node.left)
            
            node.left = None  
            self.current.right = node  
            self.current = node  
            
            inOrder(node.right)
        
        inOrder(root)
        return dummy_node.right

bst = Solution()

bst.root = TreeNode(5)
bst.root.left = TreeNode(3)
bst.root.right = TreeNode(4)
bst.root.left.left = TreeNode(2)
bst.root.left.left.left = TreeNode(1)


bst.root.right = TreeNode(6)
bst.root.right.right = TreeNode(8)
bst.root.right.right.left = TreeNode(7)
bst.root.right.right.right = TreeNode(9)