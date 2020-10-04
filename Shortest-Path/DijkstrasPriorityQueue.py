import math
class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self,val,priority):
        self.values.append([val,priority])
        self.Sort()

    def dequeue(self):
        return self.values.pop(0)      

    def helper(self,p):
        return p[1]

    def Sort(self):
          self.values.sort(key = self.helper)  

class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}
    def addVertex(self,vertex):
        if (not vertex in self.adjacencyList):
            self.adjacencyList[vertex] = []    
    def addEdge(self,v1,v2,weight):
        self.adjacencyList[v1].append([v2,weight])        
        self.adjacencyList[v2].append([v1,weight])  

    def Dijkstra(self,start,finish):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []
        for vertex in self.adjacencyList:
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex,0)     
            else:
                distances[vertex] = math.inf
                nodes.enqueue(vertex,math.inf)
            previous[vertex] = None

        while len(nodes.values):
            smallest = nodes.dequeue()[0]
            if smallest == finish: 

                while previous[smallest]:
                   path.append(smallest)
                   smallest = previous[smallest]
                break    


            if smallest or distances[smallest] != math.inf:
                for neighbour in range(len(self.adjacencyList[smallest])):
                    nextNode = self.adjacencyList[smallest][neighbour]
                    candidate = distances[smallest] + nextNode[1]
                    if candidate < distances[nextNode[0]]:
                        distances[nextNode[0]] = candidate
                        previous[nextNode[0]] = smallest
                        nodes.enqueue(nextNode[0],candidate)    
        return [y for x in [path,smallest] for y in x ][::-1]
        

w = WeightedGraph()
w.addVertex("A")
w.addVertex("B")
w.addVertex("C")
w.addVertex("D")
w.addVertex("E")
w.addVertex("F")

w.addEdge("A","B",4)
w.addEdge("A","C",2)
w.addEdge("B","E",3)
w.addEdge("C","D",2)
w.addEdge("C","F",4)
w.addEdge("D","E",3)
w.addEdge("D","F",1)
w.addEdge("E","F",1)

print(w.Dijkstra("A","F"))