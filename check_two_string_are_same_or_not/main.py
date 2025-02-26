class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1 = "".join(word1)
        
        word2 = "".join(word2)
        
        if word1 == word2:
            return True
        else:
            return False
    



word1 = ["ab", "c"]
word2 = ["a", "bc"]

s1 = Solution()
print(s1.arrayStringsAreEqual(word1, word2))