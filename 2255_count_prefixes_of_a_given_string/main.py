class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        count = 0
        
        for i in range(len(words)):
            if s.startswith(words[i]):
                count+=1
        return count
            


words = ["a","b","c","ab","bc","abc"]
s = "abc"
s1 = Solution()
print(s1.countPrefixes(words, s))