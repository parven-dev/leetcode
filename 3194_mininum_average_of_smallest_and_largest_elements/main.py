class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        
        nums = sorted(nums)
        
        end = len(nums) - 1
        
        minimum_average = []
        for i in range(len(nums)):
            if nums[i] >= nums[end]:
                break
        
            average = float((nums[i] + nums[end]) / 2)
            end-=1
            minimum_average.append(average)
            
        return min(minimum_average)
            
    
    
    
s1 = Solution()
# nums = [7,8,3,4,15,13,4,1]
nums = [4,7,5,5]
print(s1.minimumAverage(nums))
    
    