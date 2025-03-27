class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        total = 0
        
        max_value = 0
        max_value = max(nums)
        for _ in range(k):
            total+=max_value
            max_value+=1
        return total
            
            

 
s1 = Solution()    
# nums = [1,2,3,4,5]
# k = 3
nums = [5,5,5]
k = 2

print(s1.maximizeSum(nums, k))