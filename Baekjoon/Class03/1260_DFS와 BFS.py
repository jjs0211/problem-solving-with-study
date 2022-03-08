# from collections import deque

# n, m, v = map(int, input().split())
# graph = [[0]*(n+1) for _ in range(n+1)]
# visited_d = [0] * (n+1)
# visited_b = [0] * (n+1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = graph[b][a] = 1

# def dfs(v):
#     visited_d[v] = 1
#     print(v, end=' ')
#     for i in range(n+1): # 범위를 왜 이렇게 하는건지
#         if visited_d[i] == 0 and graph[i][v]: # 방문하지 않았고 연결되어 있다면
#             dfs(i)
# dfs(v)
# def bfs(start):
#     visited_b[start] = 1
#     queue = deque()
#     queue.append(start)
#     while queue:
#         v = queue.popleft()
#         print(v, end =' ')
#         for i in range(n+1):
#             if visited_b[i] == 0 and graph[i][v]:
#                 queue.append(i)
#                 visited_b[i] = 1
# print()
# bfs(v)

# from collections import deque
# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in range(1, n+1):
#     graph[i].sort()

# def dfs(v):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)

# def bfs(v):
#     visited[v] = True
#     queue = deque()
#     queue.append(v)

#     while queue:
#         a = queue.popleft()
#         print(a, end=' ')
#         for i in graph[a]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# dfs(v)
# visited = [False] * (n+1)
# print()
# bfs(v)

n, m, v= map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
dfs(v)

visited = [False] * (n+1)
from collections import deque

def bfs(v):
    visited[v] = True
    
    queue = deque()
    queue.append(v)

    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
print()
bfs(v)