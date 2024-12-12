import math
from collections import Counter

class Solution(object):
    def __init__(self, num):
        self.num = num
        
    def majorityElement(self):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(self.num)
        for item in self.num: 
            num_len = math.floor(len(self.num) / 2)
            for key, value in counter.items():           
                if value > num_len:
                    return key
            


s1 = Solution(num = [2,2,1,1,1,2,2])
print(s1.majorityElement())
