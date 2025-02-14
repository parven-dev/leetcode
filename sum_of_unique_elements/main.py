class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        
        my_dict = {}
        
        sum = 0
        for item in range(len(nums)):
            my_dict[nums[item]] = my_dict.get(nums[item], 0) + 1
            
            
             
        for key, value in my_dict.items():
            if value <= 1:
                # print(key)
                sum+=key
                
        return sum
                




nums = [1,2,3,2]
s1 = Solution()
print(s1.sumOfUnique(nums))