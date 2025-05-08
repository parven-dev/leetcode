


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []

        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter+=1

            result.append(counter)

        return result


s1 = Solution()
nums = [8, 1, 2, 2, 3]
print(s1.smallerNumbersThanCurrent(nums))
