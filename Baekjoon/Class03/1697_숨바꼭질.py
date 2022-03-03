from collections import deque

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k: # 현재 있는 위치가 동생이 있는 위치와 같다면
            print(dist[x]) # 그 때의 시간초를 출력
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= max and not dist[nx]:
                dist[nx] = dist[x] + 1 # 현재 위치에서 다음 위치로 가는데 1초가 걸리므로
                q.append(nx) # 처음에는 q에 4, 6, 10이 들어가게됨


max = 10**5
dist = [0] * (max + 1)
n, k = map(int, input().split())
bfs()