class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        adj_list = {item:[] for item in range(n)}
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        
        queue = [source]
        visited = set()
        
        while queue:
            
            dequeue = queue.pop(0)
            
            if dequeue == destination:
                return True
            
            for other_nodes in adj_list[dequeue]:
                if other_nodes not in visited:
                    visited.add(other_nodes)
                    queue.append(other_nodes)
                    
        return False
                    
            
    
    # def empty(self):
    #     return not n
        

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2


# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5
s1 = Solution()
print(s1.validPath(n, edges, source, destination))
