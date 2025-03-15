class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums+ nums
        
        
        
s1 = Solution()
nums = [1,2,3,4]
print(s1.getConcatenation(nums))