
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
         
         
class Solution:
 
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if value is None:
            return False
        
        if self.root is None: 
            self.root = TreeNode(value)
            return True
        
        temp = self.root
        
        while True:
            # if value == temp.val:
            #     return False
            
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
        
    
    
    def inOrderTraveral(self, root, my_dict):
        if not root:
            return
        self.inOrderTraveral(root.left, my_dict)
        my_dict[root.val] = my_dict.get(root.val, 0) + 1
        self.inOrderTraveral(root.right, my_dict)
        
    def findMode(self) -> list[int]:
        my_dict = {}
        
        result = []
        self.inOrderTraveral(self.root, my_dict)
        
            
        max_value = max(my_dict.values()) if my_dict else 0
        for key, value in my_dict.items():
            if value == max_value:
                result.append(key)

        return result
    
        # for value in my_dict.keys():
        #         result.append(value)
            
        # max_value = max(result)
        # print(max_value, result)
        # data= []
        # for item in result:
        #     if item == max_value:
        #         data.append(item)
        
        # return result
    
   
        
            
    
root = [1,None, 2, 2,]
# root = [0]
# root = [1,None,2]

s1 = Solution()
for value in root:
    s1.insert(value)
    
# print(s1.root.val)
print(s1.findMode())
