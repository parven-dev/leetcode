class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        index = 0
        data = []
        while index <= len(nums)-k:
            sums = 0
            for item in nums[index:index+k]:
                sums+=item
            index+=1
            data.append(sums)
        
        results = []  
        for nums in data:
            result = nums/k
            results.append(result)
            
        return max(results)
            
                

s1 = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(s1.findMaxAverage(nums, k))