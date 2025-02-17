# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrderTraversal(self, p, q):
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False
      
        left = self.postOrderTraversal(p.left, q.left)
        right = self.postOrderTraversal(p.right, q.right)
        
        return p.val == q.val and left and right
    
        
        
    def isSameTree(self, p, q) -> bool:
        
        return self.postOrderTraversal(p, q)