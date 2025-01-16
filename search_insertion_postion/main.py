class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        
        while left <=   right:
            middle = (right + left) // 2
            
            if target == nums[middle]:
                return middle
            
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
                
        return left
            
        

# nums = [1,3,5,6]
# target = 5

nums = [1,3,5,6]
target = 0

s1 = Solution()
print(s1.searchInsert(nums, target))
