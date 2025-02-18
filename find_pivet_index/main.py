class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sums = sum(nums)
        left = 0
        
        for i in range(len(nums)):
            right = sums - left - nums[i]
            
            if right == left:
                return i
            else:
                left += nums[i]
            
        return -1
          
            
            
s1 = Solution()
nums = [1,7,3,6,5,6]

print(s1.pivotIndex(nums))

