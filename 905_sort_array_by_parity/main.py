class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even = []
        odd = []
        
        for num in nums:
            
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd





nums = [3,1,2,4]
nums = [0]
s1 = Solution()
print(s1.sortArrayByParity(nums))