from collections import deque

def bfs(graph, a, b):
    global cnt_bfs

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    cnt_bfs += 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx >= n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt_bfs += 1
                queue.append((nx, ny))

    return


n = int(input())

cnt = 0
graph = []

cnt_result = []
for _ in range(n):
    graph.append(list(map(int, input())))

for a in range(n):
    for b in range(n):
        cnt_bfs = 0
        if graph[a][b] == 1:
            bfs(graph, a, b)
            cnt += 1
            cnt_result.append(cnt_bfs)
print(cnt)
for i in sorted(cnt_result):
    print(i)

# 유기농배추랑 비슷