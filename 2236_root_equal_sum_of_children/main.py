# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
class Solution():       
    def insert_level_order(self,arr, root, i, n):
            
            if i < n :
                if arr[i] is not None:
                    temp = TreeNode(arr[i])
                    root = temp
                    root.left = self.insert_level_order(arr, root.left, 2 * i + 1, n)
                    root.right = self.insert_level_order(arr, root.right, 2 * i + 2, n)
            return root
    
        
    def checkTree(self, root) -> bool:
        
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
        
        left_val = root.left.val if root.left else 0
        right_val = root.right.val if root.right else 0
        
        if left_val + right_val == root.val:
            return self.checkTree(root.left) and self.checkTree(root.right)
        else:
            return False
    



arr = [10,4,6]
arr_len = len(arr)

s1 = Solution()
root = s1.insert_level_order(arr, None, 0, arr_len)



print(s1.checkTree(root))

# print(root.val)
# print(root.left.val)
# print(root.right.val)