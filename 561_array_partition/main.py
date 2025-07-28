class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        group1 = []
        group2 = []
        for i in range(0, len(nums), 2):
            group1.append(nums[i])

        for j in range(1, len(nums), 2):
            group2.append(nums[j])

        group1_group2 = zip(group1, group2)

        total = 0
        for item in group1_group2:
            total+=min(item)

        return total