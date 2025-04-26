class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        print(arr1, arr2)

        paired = [ list(item) for item in zip(arr1, arr2)]
        
        result = []
        for item in paired:
            result.extend(item)
            
        return result
            

# nums = [2,5,1,3,4,7]
# n = 3
nums = [2,7]
n = 1
s1 = Solution()
print(s1.shuffle(nums, n))