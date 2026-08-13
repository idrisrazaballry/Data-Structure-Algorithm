def maze_problem(maze):
    print("Oroginal maze")
    for i in maze:
        for j in i:
            print(j, end=" ")
        print()

    row = len(maze)
    col = len(maze[0])

    result = [[0 for i in range(col)] for j in range(row)]

    # to check path is present or not
    def is_safe(x, y):
        if x >= 0 and x > row: # to check new are in boundary
            return False
        elif y >= 0 and y > col:
            return False
        elif maze[x][y] != 1: # cell value is safe or not
            return False
        return True
    
    def solution(x, y):
        if x == row-1 and y == col-1:
            if maze[x][y] != 1:
                return False
            result[x][y] == 1
            return True

        if is_safe(x, y):
            result[x][y] = 1
            if solution(x, y+1): # to move forward
                return True
            if solution(x+1, y): # to move downward
                return True
            result[x][y] = 0
        return False
    
    if solution(0, 0):
        return result
    else:
        return "No path found in maze"


maze = [
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1]
]

res = maze_problem(maze)
if isinstance(res, list):
    print("Resultant path :")
    for i in res:
        for j in i:
            print(j, end=" ")
        print()
else:
    print(res)
