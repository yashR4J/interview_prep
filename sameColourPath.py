RED = "red"
YELLOW = "yellow"
class Vertex():
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour
    
    def getIndex(self):
        return self.number - 1
    
    def getColour(self):
        return self.colour

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
            print("Vertex ", v1.getIndex(), " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self.graph:
            print("Vertex ", v2.getIndex(), " does not exist.")
        else:
            # Since this code is not restricted to a directed or 
            # an undirected graph, an edge between v1 v2 does not
            # imply that an edge exists between v2 and v1
            self.graph[v1].append(v2)

    # Print the graph
    def printGraph(self):
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                print(vertex.getIndex(), " -> ", edge.getIndex())

    def getAdjacencyList(self):
        for i, k in enumerate(self.graph):
            if len(self.graph[k]) == 0: continue
            print(k.getIndex(), " -> ", [x.getIndex() for x in self.graph[k]], end=" \t| ")

    # def bfs(self, root):
    #     visited, queue = [], []
    #     visited.append(root)
    #     queue.append(root)
    #     while queue:
    #         s = queue.pop(0) 
    #         for neighbour in self.graph[s]:
    #             if neighbour not in visited:
    #                 visited.append(neighbour)
    #                 queue.append(neighbour)
    #     return visited
    
    def dfs(self, root, dp, vis, path):
        vis.add(root)
        
        path[root.getIndex()] = [root.getIndex() + 1]
            
        for neighbour in self.graph[root]:
            if neighbour not in vis:
                self.dfs(neighbour, dp, vis, path)
            
                rl1, ml1 = dp[root.getIndex()]
                rl2, ml2 = dp[neighbour.getIndex()]
                
                if neighbour.getColour() == root.getColour(): # matching colour
                    rl1 += rl2
                    
                # max of running sum or old maximum
                if rl1 > ml2: # running sum is greater = root is added to path
                    ml1 = rl1
                    path[root.getIndex()] += path[neighbour.getIndex()]
                else: 
                    ml1 = ml2
                    
                dp[root.getIndex()] = rl1, ml1
    
    def longestPath(self, root):
        dp = [(1, 1) for _ in range(self.vertices_no)] 
        vis = set()
        path = [[] for _ in range(self.vertices_no)]
        
        self.dfs(root, dp, vis, path)
        ans = 0
        for i in range(self.vertices_no):
            ans = max(ans, dp[i][1])
    
        for i in range(self.vertices_no):
            if dp[i][0] == ans:
                return path[i]  

        return None
    
def test1():
    graph = Graph()  
    v1 = Vertex(1,YELLOW)
    v2 = Vertex(2,RED)
    v3 = Vertex(3,RED)
    v4 = Vertex(4,YELLOW)
    v5 = Vertex(5,RED)
    v6 = Vertex(6,YELLOW)
    v7 = Vertex(7,RED)
    v8 = Vertex(8,YELLOW)
    graph.addVertices([v1,v2,v3,v4,v5,v6,v7,v8])
    graph.addEdge(v1, v2)
    graph.addEdge(v2, v3)
    graph.addEdge(v3, v4)
    graph.addEdge(v2, v5)
    graph.addEdge(v5, v6)
    graph.addEdge(v6, v7)
    graph.addEdge(v7, v8)
    
    assert len(graph.longestPath(v1)) == 3
    assert sorted(graph.longestPath(v1)) == [2, 3, 5]

def test2():
    graph = Graph()  
    v1 = Vertex(1,YELLOW)
    v2 = Vertex(2,RED)
    v3 = Vertex(3,RED)
    v4 = Vertex(4,RED)
    v5 = Vertex(5,YELLOW)
    v6 = Vertex(6,YELLOW)
    v7 = Vertex(7,RED)
    v8 = Vertex(8,YELLOW)
    v9 = Vertex(9,RED)
    v10 = Vertex(10,RED)
    v11 = Vertex(11,YELLOW)
    v12 = Vertex(12,YELLOW)
    v13 = Vertex(13,YELLOW)
    graph.addVertices([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13])
    graph.addEdge(v1, v2)
    graph.addEdge(v2, v3)
    graph.addEdge(v2, v5)
    graph.addEdge(v2, v7)
    graph.addEdge(v7, v6)
    graph.addEdge(v5, v4)
    graph.addEdge(v5, v8)
    graph.addEdge(v8, v9)
    graph.addEdge(v9, v10)
    graph.addEdge(v8, v11)
    graph.addEdge(v11, v12)
    graph.addEdge(v12, v13)
    assert len(graph.longestPath(v1)) == 5
    assert sorted(graph.longestPath(v1)) == [5, 8, 11, 12, 13]

def test3():
    graph = Graph()  
    v1 = Vertex(1,YELLOW)
    v2 = Vertex(2,RED)
    v3 = Vertex(3,RED)
    v4 = Vertex(4,RED)
    v5 = Vertex(5,RED)
    v6 = Vertex(6,RED)
    v7 = Vertex(7,RED)
    v8 = Vertex(8,RED)
    graph.addVertices([v1,v2,v3,v4,v5,v6,v7,v8])
    graph.addEdge(v1, v2)
    graph.addEdge(v2, v3)
    graph.addEdge(v2, v5)
    graph.addEdge(v2, v7)
    graph.addEdge(v3, v4)
    graph.addEdge(v5, v6)
    graph.addEdge(v7, v8)
    assert len(graph.longestPath(v1)) == 7
    assert sorted(graph.longestPath(v1)) == [2, 3, 4, 5, 6, 7, 8]

def test4():
    graph = Graph()  
    v1 = Vertex(1,YELLOW)
    v2 = Vertex(2,RED)
    v3 = Vertex(3,YELLOW)
    v4 = Vertex(4,YELLOW)
    v5 = Vertex(5,YELLOW)
    v6 = Vertex(6,YELLOW)
    graph.addVertices([v1,v2,v3,v4,v5,v6])
    graph.addEdge(v1, v2)
    graph.addEdge(v2, v3)
    graph.addEdge(v3, v4)
    graph.addEdge(v1, v5)
    graph.addEdge(v5, v6)
    assert len(graph.longestPath(v1)) == 3
    assert sorted(graph.longestPath(v1)) == [1, 5, 6]
        
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()