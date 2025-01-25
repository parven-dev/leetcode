class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        my_dict = {}
        
        for item in s:
            my_dict[item] = my_dict.get(item, 0) + 1
            
        
        max_value = max(my_dict.values())
        min_value = min(my_dict.values())
        
        return min_value == max_value
        
        
            
        
    
    
    
    

# s = "abacbc"
s = "aaabb"
s1 = Solution()
print(s1.areOccurrencesEqual(s))