from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:

        sum_of_max_freq = 0
        freq = Counter(nums)
        max_value = max(freq.values())

        for value in freq.values():
            if value == max_value:
                sum_of_max_freq+=value
                
        return sum_of_max_freq


s1 = Solution()
nums = [1,2,2,3,1,4]
print(s1.maxFrequencyElements(nums))