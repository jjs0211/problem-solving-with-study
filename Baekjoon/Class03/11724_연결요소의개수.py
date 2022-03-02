from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for i in range(1, n+1):
    if visited[i] == False:
        bfs(i)
        cnt+=1
print(cnt)