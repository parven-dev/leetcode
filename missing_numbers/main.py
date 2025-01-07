class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        my_dict = {}
        my_list = ""

        n = len(nums)
        for i in range(n+1):
            my_dict[i] = True
        
        for num in my_dict:
            if num  not in nums:
                my_list+=str(num)
                
                
        return int(my_list)
        
        
s1 = Solution()

# nums = [3,0,1]
# nums = [9,6,4,2,3,5,7,0,1]
nums = [0,1]
print(s1.missingNumber(nums))