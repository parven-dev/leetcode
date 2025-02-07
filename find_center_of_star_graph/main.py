class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        first_edge = edges[0]
        second_edge = edges[1]
        
        if first_edge[0] in second_edge:
            return first_edge[0]
        else:
            return first_edge[1]
        
    
    



edges = [[1,2],[2,3],[4,2]]
s1 = Solution()
print(s1.findCenter(edges))
    
    
