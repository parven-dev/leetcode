# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        my_list = []

        def Traversal(node):
            if node is None:
                return

            Traversal(node.left)
            Traversal(node.right)
            my_list.append(node.val)

        Traversal(root)
        return my_list



        