import copy
from collections import deque
import sys

input = sys.stdin.readline
def bfs():
    queue = deque()
    copy_s = copy.deepcopy(s)
    for i in range(n):
        for j in range(m):
            if copy_s[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if copy_s[nx][ny] == 0:
                copy_s[nx][ny] = 2
                queue.append((nx, ny))

    cnt = 0
    global answer
    for i in range(n):
        cnt += copy_s[i].count(0)
        answer = max(answer, cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if s[i][j] == 0:
                s[i][j] = 1
                wall(cnt+1)
                s[i][j] = 0


n, m = map(int, input().split())
s = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    s.append(list(map(int, input().split())))
    
answer = 0
wall(0)
print(answer)
