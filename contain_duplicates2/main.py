class Solution(object):
    def containsNearbyDuplicate(self, nums:list, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        data = []
        for i , j in enumerate(nums):            
            value = abs(i-j) == k
            if  j in data and value <= k:
                return True
        
        return False
        
    
s1 = Solution()
    
nums = [1,2,3,1]
k = 3
print(s1.containsNearbyDuplicate(nums, k))
