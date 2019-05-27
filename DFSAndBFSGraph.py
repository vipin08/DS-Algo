from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,v):
        # v is the starting vertix
        # mark all vertices not  visited
        visited = [False]*(len(self.graph))
        # call DFS Helper
        self.DFSUtil(v, visited)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v)

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g)

g.DFS(2)



class BGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addBEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,v):
        visited = [False]*len(self.graph)
        queue = []
        queue.append(v)
        visited[s] = True
        while queue:
            v = queue.pop(0)
            print(v, end=" ")

            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

