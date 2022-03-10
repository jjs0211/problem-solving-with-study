from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(i):
    bacon = [0] * (n+1)
    visited[i] = True
    queue = deque()
    queue.append(i)

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                bacon[i] = bacon[x] + 1
                visited[i] = True
                queue.append(i)
    return sum(bacon)

result = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    result.append(bfs(i))

print(result.index(min(result))+1)