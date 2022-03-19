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
    def addEdge(self, v1, v2):
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
            self.graph[v1].append(v2)

    # Print the graph
    def printGraph(self):
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                print(vertex.getNumber(), " -> ", edge.getNumber())

    def getAdjacencyList(self):
        for i, k in enumerate(self.graph):
            if len(self.graph[k]) == 0: continue
            print(k.getNumber(), " -> ", [x.getNumber() for x in self.graph[k]], end=" \t| ")

    def bfs(self, root):
        visited, queue = [], []
        visited.append(root)
        queue.append(root)
        while queue:
            s = queue.pop(0) 
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

    def findFather(self, node):
        for vertex in self.graph:
            if node in self.graph[vertex]:
                return vertex
        return None
    
    def colourANode(self):
        def _cost(l):
            _sum = 0
            for i in range(len(l)):
                _sum += (i + 1) * l[i].getWeight()
            return _sum

        arr = self.bfs(self.root)
        seq = list()
        _set = set()
        seq.append(self.root)
        _set.add(self.root)

        for t in range(2, len(self.graph) + 2):
            max_cost = -1
            maximal_vertex = None
            for vertex in arr:
                dynamic_cost = ((vertex.getWeight() * t) + _cost(seq)) / (len(seq)+1)
                if vertex not in _set and dynamic_cost > max_cost:
                    print(vertex.getNumber(), " has cost of ", dynamic_cost, " at time ", t)
                    maximal_vertex = vertex
            if maximal_vertex == None: break
            print("maximal_vertex is ", maximal_vertex.getNumber())
            while self.findFather(maximal_vertex) not in _set:
                maximal_vertex = self.findFather(maximal_vertex)
            seq.append(maximal_vertex)
            _set.add(maximal_vertex)
        
        return seq


# driver code
graph = Graph()
# stores the number of vertices in the graph
v1 = Vertex(1,1)
v2 = Vertex(2,6)
v3 = Vertex(3,2)
v4 = Vertex(4,1)
v5 = Vertex(5,9)
graph.addVertices([v1,v2,v3,v4,v5])
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
graph.addEdge(v1, v2)
graph.addEdge(v1, v3)
graph.addEdge(v2, v4)
graph.addEdge(v3, v5)
# graph.printGraph()
# print(graph.getAdjacencyList())
# graph = Graph()
# v1 = Vertex(1,1)
# v2 = Vertex(2,2)
# v3 = Vertex(3,1)
# v4 = Vertex(4,2)
# v5 = Vertex(5,4)
# graph.addVertices([v1,v2,v3,v4,v5])
# graph.addEdge(v1, v2)
# graph.addEdge(v1, v3)
# graph.addEdge(v2, v4)
# graph.addEdge(v3, v5)
seq = graph.colourANode()
print([x.getNumber() for x in seq])