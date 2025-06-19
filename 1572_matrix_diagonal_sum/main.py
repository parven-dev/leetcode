class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        row = len(mat)
        col = len(mat[0])

        total = 0

        for i in range(row):
            diagonal = mat[i][col-i-1]
            total+=diagonal
            

        for j in range(row-1, -1, -1):
            reverse_diagonal = mat[j][j]
            total+=reverse_diagonal
            

        if row  % 2 == 1:
            center = row // 2
            total -= mat[center][center]
            
        return total
    
s1 = Solution()
mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
print(s1.diagonalSum(mat))