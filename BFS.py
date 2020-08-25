from collections import deque

def BFS(graph, v, visited):
    visited[v] = True

    queue = deque([v])

    while queue :
        v = queue.popleft()
        print(v, end=' ')

        for node in graph[v]:
            if not visited[node] :
                queue.append(node)
                visited[node] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]  

visited = [False] * len(graph)

BFS(graph, 1, visited)