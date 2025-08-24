class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        
        target = []
        
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
            
        return target
    
    

s1 = Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(s1.createTargetArray(nums, index))from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count_values = Counter(arr)
        
        store_frequcency = []
        for key in count_values.keys():
            store_frequcency.append(count_values[key])
        
        return len(set(store_frequcency)) == len(store_frequcency)
            
        
        
        
    
    
s1 = Solution()
print(s1.uniqueOccurrences(arr = [1,2,2,1,1,3]))
