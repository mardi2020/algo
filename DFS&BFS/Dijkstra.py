import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력
n, m = map(int, input().split())
start = int(input())

#  초기화
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

# 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중, 가장 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    idx = 0

    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    #시작 노드 제외
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        #연결된 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]] :
                distance[j[0]] = cost


dijkstra(start)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1) :
    if distance[i] == INF :
        print("INFINITY")
    else:
        print(distance[i])