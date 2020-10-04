class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}
    def addVertex(self,vertex):
        if (not vertex in self.adjacencyList):
            self.adjacencyList[vertex] = []    
    def addEdge(self,v1,v2,weight):
        self.adjacencyList[v1].append([v2,weight])        
        self.adjacencyList[v2].append([v1,weight])     

w = WeightedGraph()
w.addVertex("A")
w.addVertex("B")
w.addVertex("C")

w.addEdge("A","B",9)
w.addEdge("A","C",5)
w.addEdge("B","C",7)

print(w.adjacencyList)

      