class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        
        one_list = []
        for array in grid:
            one_list+=array
            
        k = k % len(one_list)

        
        one_complete_list = one_list[-k:] + one_list[:-k]
        
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                grid[row][col] = one_complete_list[row * len(grid[0]) + col]
                
        return  grid
    
    
    
    
    
s1 = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(s1.shiftGrid(grid, k)) 
