class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        total_negative_nums = 0
        
        for row in grid:
            for i in range(len(row)):
                if row[i] < 0:
                    total_negative_nums+=1
                else:
                    pass
        return total_negative_nums
    


s1 = Solution()    
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(s1.countNegatives(grid))