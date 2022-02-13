import math

def graphDistances(g, s):
    def getLowestDistanceNode(queue, dist):
        node = None
        lowest_d = math.inf
        for v in queue:
            if dist[v] <= lowest_d:
                lowest_d = dist[v]
                node = v
        queue.remove(node)
        return node   
        
    queue = [x for x in range(len(g))]
    dist = [math.inf for _ in range(len(g))]
    dist[s] = 0
    while len(queue) != 0:
        nextNode = getLowestDistanceNode(queue, dist)
        for vertex, weight in enumerate(g[nextNode]):
            if weight == -1: continue
            newD = dist[nextNode] + weight
            if newD < dist[vertex]:
                dist[vertex] = newD
                
    return dist