class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        
        if len(nums1) >  len(nums2):
            nums1, nums2 = nums2, nums1

        for item in nums1:
            left  = 0
            right = len(nums2) - 1
            while left <= right:
                middle = (left + right) // 2
                
                if item == nums2[middle]:
                    return item

                
                elif item < nums2[middle]:
                    right = middle - 1
                    
                else:
                    left = middle + 1
        
        return -1
            
                  
    
    
# nums1 = [1,2,3]
# nums2 = [2,4]  

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
s1 = Solution()

print(s1.getCommon(nums1, nums2))
