[200~class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_sum = [0]
        right_sum = [] 
        
        for i in range(1, len(nums)):
            left = nums[:i]
            right = nums[i:]
            left_sum.append(sum(left))
            right_sum.append(sum(right))
        
        right_sum = right_sum + [0]
        
        result = [abs(a- b) for a, b in zip(left_sum, right_sum)]
        return result
    
    
    

s1 = Solution()
print(s1.leftRightDifference(nums = [10,4,8,3]))
