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
    
    def inOrderTraversal(self, node, result =None):
        if result is None:
            result = []
        
        if node:
            self.inOrderTraversal(node.left, result)
            result.append(node.val)
            self.inOrderTraversal(node.right, result)
            
        return result
        
        
    def getMinimumDifference(self):
        result = self.inOrderTraversal(self.root)
        # my_lit = []
        
        min_value = float("inf")
        for item in range(len(result)-1):
            my_data = result[item+1] - result[item]
            
            if my_data < min_value:
                min_value = my_data
                
        return min_value
            
            # my_lit.append(my_data)
            
        # return min(my_lit)
    
    
    # def getMinimumDifference(self):
    #     for item in self.root.result:
    #         print(item)
                

root  = [4,2,6,1,3]  
s1 = Solution()

for value in root:
    s1.insert(value)
    

print(s1.getMinimumDifference())
# print(s1.inOrderTraversal(s1.root))
# print(s1.getMinimumDifference())

# print(s1.root.val)
# print(s1.root.right.val)
# print(s1.root.left.val)


# s1.insert(2)
# s1.insert(1)
# s1.insert(3)

# print(s1.root.val)
# print(s1.root.left.val)
# print(s1.root.right.val)

# print(s1.getMinimumDifference(root))     