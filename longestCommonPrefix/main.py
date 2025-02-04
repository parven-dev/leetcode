class Solution:
    
   
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        low = 0
        high = min(len(string) for string in strs)
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.check_middle(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        
        if len(strs) == 0:
            return ""  
        
        else:
            return strs[0][:high]
            
            
        
        
    def check_middle(self,strs, mid_value):
        for item in strs:
            if item[:mid_value] != strs[0][:mid_value]:
                return False
        return True
            
            
    
    
    

strs = ["flower","flow","flight"]
s1 = Solution()
print(s1.longestCommonPrefix(strs))
