class Solution:
    def repeatedCharacter(self, s: str) -> str:
        result = set()
        ans  = ""
        for i in range(len(s)):
            if s[i] in result:
                return s[i]
            result.add(s[i])
            
        return ans
    
    
s = "abccbaacz"
s1 = Solution()
result = s1.repeatedCharacter(s)
print(result)