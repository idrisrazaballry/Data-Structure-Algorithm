INF = 999

def display(graph):
    for i in graph:
        for j in i:
            if j == INF:
                print('INF', end=" ")
            else:
                print(j, end=" ")
        print()

def folyd_warshall_algo(graph):
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    print()
    display(graph)


graph = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 9, 2, 0]
]

display(graph)
folyd_warshall_algo(graph)
