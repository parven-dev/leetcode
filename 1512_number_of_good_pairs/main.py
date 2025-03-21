class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = my_dict.get(nums[i],0)+1
        
        sums = 0
        
        for value in my_dict.values():
            sums += (value * (value - 1)) // 2 
                
        return sums
    
nums = [1,2,3,1,1,3]
s1 = Solution()
print(s1.numIdenticalPairs(nums))
