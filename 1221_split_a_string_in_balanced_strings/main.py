class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        balanced = 0
        track_string = 0
        
        for i in range(len(s)):
         
            if s[i] == "R":
                balanced+=1
                
            elif s[i]  == "L":
                balanced-=1
                
            if balanced == 0:
                track_string+=1
                
          
        return track_string
 
s1 = Solution()
# s = "RLRRLLRLRL"
s = "RLRRRLLRLL"
print(s1.balancedStringSplit(s))