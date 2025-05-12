class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_value = []
        for arr in accounts:
            max_value.append(sum(arr))
            
        return max(max_value)
    
    
s1 = Solution()
result = s1.maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]])
print(result)