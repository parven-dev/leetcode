import math

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        total = sum(nums)

        for _ in nums:
            reminder = total % k
            if reminder == 0:
                return reminder
            else:
                pass
        return reminder
s1 = Solution()
nums = [3,9,7]
k = 5
print(s1.minOperations(nums, k))