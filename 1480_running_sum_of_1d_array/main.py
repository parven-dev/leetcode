class Solution:
    
    def runningSum(self, nums: list[int]) -> list[int]:
        my_list = []
        total = 0
        for i in range(len(nums)):
            total +=nums[i]
            my_list.append(total)
        return my_list
    
    
nums = [1,2,3,4]
s1 = Solution()
print(s1.runningSum(nums))