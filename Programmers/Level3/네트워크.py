from collections import deque
def solution(n, computers):
    visited = [False] * n
    cnt = 0

    def bfs(start): 
        queue = deque()
        queue.append(start)
        visited[start] = True
        nonlocal cnt

        while queue:
            v = queue.popleft()
            for i in range(len(computers[v])):
                if not visited[i] and computers[v][i] ==1:
                    visited[i] = True
                    queue.append(i)
                    cnt+=1

    for i in range(n): # 0, 1, 2
        bfs(i)

    return n-cnt