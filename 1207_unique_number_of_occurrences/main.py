from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count_values = Counter(arr)
        
        store_frequcency = []
        for key in count_values.keys():
            store_frequcency.append(count_values[key])
        
        return len(set(store_frequcency)) == len(store_frequcency)
            
        
        
        
    
    
s1 = Solution()
print(s1.uniqueOccurrences(arr = [1,2,2,1,1,3]))
