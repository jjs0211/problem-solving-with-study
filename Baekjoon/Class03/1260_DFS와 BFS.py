from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited_d = [0] * (n+1)
visited_b = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited_d[v] = 1
    print(v, end=' ')
    for i in range(n+1): # 범위를 왜 이렇게 하는건지
        if visited_d[i] == 0 and graph[i][v]: # 방문하지 않았고 연결되어 있다면
            dfs(i)
dfs(v)
def bfs(start):
    visited_b[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in range(n+1):
            if visited_b[i] == 0 and graph[i][v]:
                queue.append(i)
                visited_b[i] = 1
print()
bfs(v)