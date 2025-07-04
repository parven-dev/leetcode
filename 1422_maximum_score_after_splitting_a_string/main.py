class Solution:
    def maxScore(self, s: str) -> int:
        
        max_score = 0
        
        for i in range(1,len(s)):
            right_string = s[i:]
            left_string = s[:i]
            
            count_zero = left_string.count('0')
            count_one = right_string.count('1')
            total_count = count_one + count_zero
            max_score = max(max_score, total_count)
    
        return max_score
 
 
s1 = Solution()   
s = "011101"
print(s1.maxScore(s))