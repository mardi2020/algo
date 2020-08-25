#n, m = map(int, input().split())
n, m = 4, 5
graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
#graph = []
visited = []

for _ in range(n):
    #graph.append(list(map(int, input())))
    visited.append([False]*m)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y) :
    visited[x][y] = True
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if newX >= 0 and newY >= 0 and newX < n and newY < m :
            if not visited[newX][newY] and not graph[newX][newY] :
                graph[newX][newY] = 1
                dfs(newX, newY)


ice = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 :
            dfs(i, j)
            ice += 1


print(ice)
        




