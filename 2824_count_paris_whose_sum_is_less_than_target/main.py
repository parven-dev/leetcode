class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        counter = 0
        left = 0
        right = len(nums)-1
        
        sorted_nums = sorted(nums)
                
        while left < right:
            if sorted_nums[left] + sorted_nums[right] < target:
                counter+=(right-left)
                left+=1
            else:
                right-=1
              
        return counter
    
nums = [-1,1,2,3,1]
target = 2
s1 = Solution()
print(s1.countPairs(nums, target))