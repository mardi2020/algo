from collections import deque

n, m = map(int, input().split())
mapp = []
for _ in range(n):
    mapp.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m :
                if mapp[nx][ny] == 1 :
                    mapp[nx][ny] = mapp[x][y] + 1
                    queue.append((nx, ny))
                    
    return mapp[n-1][m-1]


print(bfs(0, 0))