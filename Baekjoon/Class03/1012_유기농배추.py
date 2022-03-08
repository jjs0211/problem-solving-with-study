# from collections import deque

# def bfs(graph, a, b):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     queue = deque()
#     queue.append((a,b))
#     graph[a][b] = 0

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx<0 or nx >= n or ny<0 or ny>=m:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))
#     return


# t = int(input())
# for _ in range(t):
#     cnt = 0
#     m, n, k = map(int, input().split())  # 가로, 세로, 심어져있는 배추의 수
#     graph = [[0]*m for _ in range(n)]
#     for _ in range(k):
#         a, b = map(int, input().split())
#         graph[b][a] = 1
#     for a in range(n):
#         for b in range(m):
#             if graph[a][b] == 1: # 그래프를 다 돌면서 1인 부분이 있다면 bfs를 통해 1과 그 주변의 1들을 다 0으로 만들어줌
#                 bfs(graph, a, b)
#                 cnt+=1
#     print(cnt)



from collections import deque
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a]= 1


    def bfs(graph, a, b):
        
        queue = deque()
        queue.append((a,b))
        graph[a][b] = 0

        while queue:
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
            
            

    cnt = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)