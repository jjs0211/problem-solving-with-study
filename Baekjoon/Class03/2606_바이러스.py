# computer_cnt = int(input())
# network = int(input())
# graph = [[0]*(computer_cnt+1) for _ in range(computer_cnt+1)]
# visited_d = [0] * (computer_cnt+1)
# result = 0
# for _ in range(network):
#     a, b = map(int, input().split())
#     graph[a][b] = graph[b][a] = 1
#
# def dfs(v):
#     global result
#     visited_d[v] = 1
#     for i in range(computer_cnt+1):
#         if visited_d[i] == 0 and graph[i][v]:
#             dfs(i)
#             result += 1
# dfs(1)
# print(result)


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
def dfs(v):
    visited[v] = True
    global cnt
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            cnt+=1
dfs(1)
print(cnt)