class Solution:
    def minOperations(self, nums: list[int]) -> int:
        
        increamented_operations = 0

        for i in range(1, len(nums)):
          
          j = i - 1
          if nums[j] >= nums[i]:
              increament_value = nums[j] - nums[i] + 1
              print(increament_value)
              nums[i] += increament_value
              increamented_operations += increament_value
              
        return increamented_operations


nums = [1,1,1]
s1 = Solution()
print(s1.minOperations(nums))