class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        result = []
        for i in range(len(nums)):
            if nums[i] < 0:
                if abs(nums[i]) in nums:
                    result.append(abs(nums[i]))

        if result:
            return max(result)
        else:
            return -1
    
s1 = Solution()
nums = [-10,8,6,7,-2,-3]
print(s1.findMaxK(nums=nums))
    