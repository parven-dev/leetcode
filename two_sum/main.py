class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for item in range(len(nums)):
            for items in (item +1,  len(nums)):
                print(nums[items])
            
            

s1 = Solution()
print(s1.twoSum(nums=[2,7,11,15], target=9))
