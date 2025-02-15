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
        if value == None:
            return False
        
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
        
    def inOrderTraversal(self,root, result):
        if not root:
            return
        self.inOrderTraversal(root.left, result)
        result.append(root.val)
        self.inOrderTraversal(root.right, result)
        
        
    
    
    def rangeSumBST(self, low: int, high: int) -> int:
        result = []
        sum = 0
        self.inOrderTraversal(self.root, result)
        
        
        for item in result:
            if low <= item <= high:
                sum += item
        return sum
        
        # while low <= node <= high:
            
    
   
        
    

# root = [10,5,15,3,7,None,18]
# low = 7
# high = 15    
root = [10,5,15,3,7,13,18,1,None,6]
low = 6
high = 10
s1 = Solution()

for value in root:
    s1.insert(value)
    

print(s1.rangeSumBST(low, high))