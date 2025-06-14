class Solution:
    def buildArray(self, nums: list[int]) ->list[int]:
        
        result = [0] * len(nums)
        
        for i in range(len(nums)):
            result[i] = nums[nums[i]]
        return result
    
    
    
s1 = Solution()
nums = [5,0,1,2,3,4]
print(s1.buildArray(nums))