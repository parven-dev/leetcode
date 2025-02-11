# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
         
         
class Solution:
 
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        
        if self.root is None: 
            self.root = TreeNode(value)
            return True
        
        temp = self.root
        
        while True:
            if value == temp.val:
                return False
            
            if value < temp.val:
                if temp.left is None:
                    temp.left = TreeNode(value)
                    return True
                
                temp = temp.left
                
            else:
                if temp.right is None:
                    temp.right = TreeNode(value)
                    return True
                temp = temp.right
                
                
    
    def inOrderTraversal(self, node, my_list):
        if not node:
            return 
        
        my_list.append(node.val)
        self.inOrderTraversal(node.left, my_list)
        self.inOrderTraversal(node.right, my_list)
        
        
                
                
    def searchBST(self, val: int):
        current = self.root
        while current is not None:
            if val == current.val:
                my_list  = []
                self.inOrderTraversal(current, my_list)
                return my_list
    
            elif val < current.val:
                current = current.left
            else:
                current = current.right
                
        return None
    
    
                
        


root = [4,2,7,1,3]
val = 2

# root = [4,2,7,1,3]
# val = 5
s1 = Solution()
for value in root:
    s1.insert(value)
    
# print(s1.root.left.val)
print(s1.searchBST(val))

