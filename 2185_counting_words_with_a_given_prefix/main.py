class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        
        count = 0
        for item in words:
            if item.startswith(pref):
                count+=1
                
        return count
            
    

words = ["pay","attention","practice","attend"]
pref = "at"
s1 = Solution()
print(s1.prefixCount(words, pref))