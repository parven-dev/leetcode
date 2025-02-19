class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
        
    def bsf(self, vertex, vertex2):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deleted_vertex = queue.pop(0)
            
            if deleted_vertex == vertex2:
                return True
            for adjcent in self.gdict.get(deleted_vertex, []):
                if adjcent not in visited:
                    visited.append(adjcent)
                    queue.append(adjcent)
        return False
    
    
        
   

gdict = {
    "A": ["B", "C", "D"],
    "B": ["J"],
    "C": ["G"],
    "D":[],
    "E": ["F", "A"],
    "F": ["I"],
    "G": ["H", "D"],
    "H": [],
    "I": [],
    "J": []
    
}   

graph = Graph(gdict)
print(graph.bsf("B", "J"))
