class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        arr = []
        
        for num in nums:
            if num%2 == 0:
                arr.append(0)
            else:
                arr.append(1)
        return sorted(arr)

s1 = Solution()
nums = [1,5,1,4,2]
print(s1.transformArray(nums))