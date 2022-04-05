from math import inf

class Vertex():
    def __init__(self, number, weight):
        self.number = number
        self.weight = weight
    
    def getNumber(self):
        return self.number
    
    def getWeight(self):
        return self.weight

class Graph():
    def __init__(self):
        self.graph = {}
        self.root = None
        self.vertices_no = 0

    # Add a vertex to the dictionary
    def addVertex(self, v):
        if len(self.graph) == 0: self.root = v
        if v in self.graph:
            print("Vertex ", v, " already exists.")
        else:
            self.vertices_no += + 1
            self.graph[v] = []
    
    def addVertices(self, l):
        for x in l:
            self.addVertex(x)

    # Add an edge between vertex v1 and v2 with edge weight e
    def addEdge(self, v1, v2, weight):
        # Check if vertex v1 is a valid vertex
        if v1 not in self.graph:
            print("Vertex ", v1.getNumber(), " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self.graph:
            print("Vertex ", v2.getNumber(), " does not exist.")
        else:
            # Since this code is not restricted to a directed or 
            # an undirected graph, an edge between v1 v2 does not
            # imply that an edge exists between v2 and v1
            self.graph[v1].append((v2, weight))

    # Print the graph
    def printGraph(self):
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                print(vertex.getNumber(), " -> ", edge[0].getNumber(), " with weight", edge[1])

    def getAdjacencyList(self):
        for i, k in enumerate(self.graph):
            if len(self.graph[k]) == 0: continue
            print(k.getNumber(), " -> ", [x[0].getNumber() for x in self.graph[k]], end=" \t| ")

    def dfs(self, root, dp):
        
        pass

    def maxLeafNodes(self):
        M = 0
        for vertex in self.graph:
            if len(self.graph[vertex]) == 1:
                M += 1
        if len(self.graph[1]) == 1:
            M -= 1
        
        N = self.vertices_no
        
        dp = dp[N + 1][M + 1]
        
        self.dfs(1, dp, M)
        
        min = inf
        leafs = 0
        for i, profit in enumerate(dp[1]):
            if 0 <= profit < min:
                leafs = i
        
        return leafs
        

# driver code
graph = Graph()
# stores the number of vertices in the graph
v1 = Vertex(1,0)
v2 = Vertex(2,0)
v3 = Vertex(3,0)
v4 = Vertex(4,1)
v5 = Vertex(5,5)
graph.addVertices([v1,v2,v3,v4,v5])
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
graph.addEdge(v1, v2, 1)
graph.addEdge(v1, v3, 1)
graph.addEdge(v2, v4, 2)
graph.addEdge(v3, v5, 4)
graph.printGraph()
