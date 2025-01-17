class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        
        left = 0
        right = len(nums) -1


    
        while left <= right:
            middle = (right + left) // 2
            
            if  nums[middle] < 0:
                left = middle + 1
            
            else:
                right = middle  - 1
                
        neg = right + 1
        
        
        left = 0
        
        right = len(nums) - 1
        
        while left <= right:
            
            middle = (left + right) // 2
            
            
            if nums[middle] > 0:
                right = middle - 1
                
            else:
                left = middle + 1
                
                
        pos = len(nums) - left
        
        
        return max(neg, pos)
                
            
            
                
        
       
            
    
    

nums = [-2,-1,-1,1,2,3]

s1 = Solution()
print(s1.maximumCount(nums))