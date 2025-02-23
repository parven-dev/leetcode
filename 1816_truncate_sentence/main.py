class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        truncate_string = s.split()
        return truncate_string[:k]
    
    
    
s = "Hello how are you Contestant"
k = 4
s1 = Solution()
print(s1.truncateSentence(s, k))