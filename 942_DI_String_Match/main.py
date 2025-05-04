class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        available_values = list(range(len(s)+1))
        result = []    
        left = 0 
        right = len(available_values)-1
        
        for i in range(len(s)):
            if s[i] == "I":
                result.append(available_values[left])
                left+=1
            if s[i] == "D":
                result.append(available_values[right])
                right-=1
        result.append(available_values[left])
        return result
    
s = "IDID"
# Output: [0,4,1,3,2]
s1 = Solution()
print(s1.diStringMatch(s))