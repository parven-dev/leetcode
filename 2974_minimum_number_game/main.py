class Solution:
    def numberGame(self, nums: list[int]) ->list[int]:
        result = []
        
        sorted_value = sorted(nums, reverse=True)
        
        while len(sorted_value) > 1:
            alice = sorted_value.pop()
            bob = sorted_value.pop()
            
            result.append(bob)
            result.append(alice)
           
        return result

s1 = Solution()

# nums = [5,4,2,3]
nums = [2,7,9,6,4,6]
print(s1.numberGame(nums))