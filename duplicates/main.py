class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        my_table = {}
        

        for item in nums:
            my_table[item] = my_table.get(item, 0) + 1
            
            
        
        print(my_table)

        
        for value in my_table.values():
            if value > 1:
                return True
        
        return False
        
        
        

# nums =  [1,2,3,1]
nums = [2,14,18,22,22]
s1 = Solution()

print(s1.containsDuplicate(nums))
