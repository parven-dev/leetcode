class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        for item in nums:
            my_dict[item] = my_dict.get(item, 0) + 1
         
        for key, value in my_dict.items():   
            if value == 1:
                return key
        
            
            
  
s1 = Solution()            
nums = [4,1,2,1,2]
nums = [2,2,1]
print(s1.singleNumber(nums))