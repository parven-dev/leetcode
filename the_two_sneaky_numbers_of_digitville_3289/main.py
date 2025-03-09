class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        sneaky_numbers = {}
        
        sneaky_numbers_list = []
        for i in range(len(nums)):
            sneaky_numbers[nums[i]] = sneaky_numbers.get(nums[i], 0) + 1
        
    
        for key, value in sneaky_numbers.items():
            if value == 2:
                sneaky_numbers_list.append(key)
                
        return sneaky_numbers_list
    


nums = [7,1,5,4,3,4,6,0,9,5,8,2]
s1 = Solution()
print(s1.getSneakyNumbers(nums))        