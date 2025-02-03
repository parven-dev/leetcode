class Solution:
    def digitCount(self, num: str) -> bool:
        
        my_dict = {}
        
        for item in num:
            my_dict[item] = my_dict.get(item, 0) + 1
        
                
                
        for i in range(len(num)):
            # print(my_dict.get(str(i), 0))
            #{'1': 0, '2': 0, '0': 0}
            
            if int(num[i]) != my_dict.get(str(i), 0):
                pass
                return False

        return True
            
            
          
    
    


s1 = Solution()
num = "1210"
print(s1.digitCount(num))
        
        
        