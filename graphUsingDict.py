class GRAPH:
    def __init__(self):
        self.graph = {}

    def display(self):
        if len(self.graph) != 0:
            for k,v in self.graph.items():
                print(k, ":", v)
        else:
            print("no vertex in graph")

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            return True
        return False

    def addEdges(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            return True
        return False

    def removeEdges(self, vertex1, vertex2):
            if vertex1 in self.graph and vertex2 in self.graph:
                self.graph[vertex1].remove(vertex2)
                self.graph[vertex2].remove(vertex1)
                return True
            return False

    def removeVertex(self, vertex):
        if vertex in self.graph:
            for adj_vertex in self.graph[vertex]:
                self.graph[adj_vertex].remove(vertex)
            del self.graph[vertex]
            return True
        return False

    def bfs_traversing(self, vertex):
        # check vertex is present or not
        # check the vertex is visited or not, if not mark it as visited and add it to queue DS
        # check if any element present in queue DS or not, if it has element pop() that ele and display and add all its adj_vertex to queue DS
        # iterate through each element iin queue and check the element visited or not and continue from the beginning
        if vertex in self.graph:
            visited = [vertex]
            queue = [vertex]

            while queue:
                delvertex = queue.pop(0)
                print(delvertex, end=" ")
                for adj_vertex in self.graph[delvertex]:
                    if adj_vertex not in visited:
                        visited.append(adj_vertex)
                        queue.append(adj_vertex)
        else:
            print("The vertex doesn't exists")

    def dfs_traversing(self, vertex):
        if vertex in self.graph:
            visited = [vertex]
            stack = [vertex]
        
            while stack:
                delvertex = stack.pop()
                print(delvertex, end=" ")
                for adj_vertex in self.graph[delvertex]:
                    if adj_vertex not in visited:
                        visited.append(adj_vertex)
                        stack.append(adj_vertex)
        else:
            print("The vertex doesn't exists")


g1 = GRAPH()
g1.addVertex('A')
g1.addVertex('B')
g1.addVertex('C')
g1.addVertex('D')
g1.addVertex('E')
g1.display()
print()
g1.addEdges('A', 'B')
g1.addEdges('A', 'C')
g1.addEdges('A', 'D')
g1.addEdges('B', 'E')
g1.addEdges('C', 'D')
g1.addEdges('D', 'E')
g1.display()
print()
g1.removeEdges('A', 'C')
g1.display()
print()
# g1.removeVertex('C')
# g1.display()
print()
print("Breadth First Search(BFS) Traversing ")
g1.bfs_traversing('A')
print()
print()
print("Depth First Search(DFS) Traversing ")
g1.dfs_traversing('A')
