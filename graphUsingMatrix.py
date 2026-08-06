class GRAPH:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0]*len(vertices) for _ in range(len(self.vertices))]
        print(self.adj_matrix)

    def display(self):
        print(" ",end=" ")
        for i in self.vertices:
            print(i, end=" ")
        print()
        for j,k in enumerate(self.adj_matrix):
            print(self.vertices[j], end=" ")
            for x in k:
                print(x, end=" ")
            print()

    def addEdges(self, vertex1, vertex2):
        # check both vertex is present or not
        # get it index number
        # modify based on index number in adj_matrix
        # v1 = input("Enter the first vertex :")
        # v2 = input("Enter the second vertex :")

        # if v1 not in self.vertices or v2 not in self.vertices:
        #     print("One or both vertices not found in graph.")
        #     return

        # i = self.vertices.index(v1)
        # j = self.vertices.index(v2)

        # self.adj_matrix[i][j] = 1
        # self.adj_matrix[j][i] = 1  # remove this line if you want a directed graph
        if vertex1 in self.vertices and vertex2 in self.vertices:
            idx1 = self.vertices.index(vertex1)
            idx2 = self.vertices.index(vertex2)
            self.adj_matrix[idx1][idx2] = 1
            self.adj_matrix[idx2][idx1] = 1
        else:
            print("vertex doesn't exist")

    def removeEdges(self,vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            idx1 = self.vertices.index(vertex1)
            idx2 = self.vertices.index(vertex2)
            self.adj_matrix[idx1][idx2] = 0
            self.adj_matrix[idx2][idx1] = 0
        else:
            print("vertex doesn't exist")

    def removeVertex(self, vertex):
        if vertex not in self.vertices:
            print("vertex doesn't exist")
            return

        idx = self.vertices.index(vertex)

        # remove the row for this vertex
        self.adj_matrix.pop(idx)

        # remove the column for this vertex from every remaining row
        for row in self.adj_matrix:
            row.pop(idx)

        # finally remove the vertex name itself
        self.vertices.pop(idx)




total = int(input("Enter the total vertex to add :"))
vertices = []

for i in range(total):
    name = input("Enter the vertex name :")
    vertices.append(name)

g1 = GRAPH(vertices)
g1.display()

# total_edges = int(input("Enter the total edges to add :"))
# for i in range(total_edges):
#     g1.addEdges()
# g1.display()


