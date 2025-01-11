class Solution:
    def romanToInt(self, s: str) -> int:
        
        my_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        sums = 0
        for i in range(len(s)):
            if i > 0 and my_dict[s[i]] > my_dict[s[i-1]]:
                
                sums += my_dict[s[i]] - my_dict[s[i-1]] * 2
            else:
                sums += my_dict[s[i]]
        
        return sums
        
s1 = Solution()

s = "LVIII"
# s = "MCMXCIV"
print(s1.romanToInt(s))
