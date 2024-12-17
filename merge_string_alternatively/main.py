
import math
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: strn
        """
        
        all_words = word1 + word2
        data = []
        for i in  range(len(all_words)):
       
            if i < len(word1) :
                    data.append(word1[i])
              
            if i < len(word2):
                data.append(word2[i])
        
        
        return "".join(data)


s1 = Solution()
word1 = "abcd"
word2 = "pq"
print(s1.mergeAlternately(word1, word2))
