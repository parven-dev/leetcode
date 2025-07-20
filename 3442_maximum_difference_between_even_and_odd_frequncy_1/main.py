
from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        
        
        my_dict = Counter(s)
        odd_max_value = 0 
        even_min_value = float("inf")
        
        for key in my_dict.keys():
            if my_dict[key] % 2 != 0:
                odd_max_value = max(my_dict[key], odd_max_value)
            else:
                even_min_value = min(my_dict[key], even_min_value)
            
        return odd_max_value - even_min_value
            
    
    
s1 = Solution()
# s = "aaaaabbc"
s = "mmsmsym"
result = s1.maxDifference(s)
print(result)
        