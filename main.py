class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        sums= 0
        
        for i in range(len(nums)):
            # print(nums[i])
            remainder = nums[i] % 3
            
            if remainder == 1:
                sums+=1
                
            elif remainder == 2:
                sums+=1
          
                
        return sums
                    
    

s1 = Solution()
nums = [1,2,3,4]
print(s1.minimumOperations(nums))