
import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        counter = 0
        for word in s:
            if word == letter:
                counter+=1
                
        return math.floor(counter / len(s) * 100)





# s = "foobar"
# letter = "o"
s = "sgawtb"
letter = "s"
s1 = Solution()
print(s1.percentageLetter(s, letter))