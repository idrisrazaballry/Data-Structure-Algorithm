# Bellman Ford Algorithm
class GRAPH:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    def addEdges(self, s, d, w):
        if s in self.vertices and d in self.vertices:
            self.edges.append([s, d, w])

    def bellmanFordAlgo(self, vertex):
        if vertex in self.vertices:
            dictionary = {i: float('inf') for i in self.vertices}
            dictionary[vertex] = 0

            # bellman ford algo
            for _ in range(len(self.vertices)-1):
                for s, d, w,  in self.edges:
                    if dictionary[d] > dictionary[s] + w:
                        dictionary[d] = dictionary[s] + w

            self.display(dictionary)
        else:
            print("vertex doesn't exists")

    def display(self, dictionary):
        for k, v in dictionary.items():
            print(k, " : ", v)


g1 = GRAPH()
g1.addVertex('A')
g1.addVertex('B')
g1.addVertex('C')
g1.addVertex('D')
g1.addVertex('E')
g1.addEdges('A', 'C', 6)
g1.addEdges('A', 'D', 6)
g1.addEdges('B', 'A', 3)
g1.addEdges('C', 'D', 2)
g1.addEdges('D', 'B', 1)
g1.addEdges('D', 'C', 1)
g1.addEdges('E', 'B', 4)
g1.addEdges('E', 'D', 2)
g1.bellmanFordAlgo('D')

