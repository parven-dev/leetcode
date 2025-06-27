class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
             
        max_value = 0
        total = 0
        for num in nums:
            if num == 1:
                total+=1
                max_value = max(max_value, total)
                
            else:
                total = 0
        return max_value
    
    
s1 =  Solution()
print(s1.findMaxConsecutiveOnes( nums = [1,1,0,1,1,1]))