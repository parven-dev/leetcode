class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if target == nums[middle]:
                return middle
            
            elif target > nums[middle] :
                left = middle + 1 
            else:
                right = middle - 1
            
            
        return -1
        
        

nums = [-1,0,3,5,9,12]
target = 9

# nums = [-1,0,3,5,9,12]
# target = 2
s1 = Solution()
print(s1.search(nums, target))