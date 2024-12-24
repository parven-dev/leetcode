class Solution(object):
    def searchInsert(self, nums:list[int], target:int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.left = 0
        self.right = len(nums) - 1
        
        while self.left <= self.right:
            middle = (self.left + self.right) // 2
            
            if target > nums[middle]:
                self.left = middle + 1
            else:
                self.right = middle - 1
        
        # At this point, self.left is the correct index for insertion
        return self.left
            

s1 = Solution()
 
nums = [1,3,5,6]
target = 2
print(s1.searchInsert(nums, target))
