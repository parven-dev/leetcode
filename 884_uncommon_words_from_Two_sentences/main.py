from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        merge_list = s1 +" " +  s2
        split_list = merge_list.split()
        hashed_list = Counter(split_list)
        result = []
        for key, value in hashed_list.items():
            if value == 1:
                result.append(key)
        return result
                
    
    
    
s1 = "this apple is sweet"
s2 = "this apple is sour"
s = Solution()
print(s.uncommonFromSentences(s1, s2))