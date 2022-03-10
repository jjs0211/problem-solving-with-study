from collections import deque
n, m = map(int, input().split())

dice_cnt = [0] * 101 # 각 칸까지의 주사위 굴린 횟수
visited = [False] * 101
ladder = dict()
snake = dict()

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        x = queue.popleft()
        
        if x == 100:
            print(dice_cnt[x])
            break
        
        for dice in range(1, 7):
            # 다음 이동할 위치는 현재 위치 + 주사위에서 나온 숫자
            next_place = x + dice

            # 이동할 위치가 맵을 벗어나지 않고 방문하지 않은 곳이라면
            if next_place <= 100 and not visited[next_place]:

                # 만약 이동할 위치에 사다리가 있다면
                if next_place in ladder.keys():
                    # 이동할 위치는 사다리 타고 이동한 곳
                    next_place = ladder[next_place]

                # 이동할 위치에 뱀이 있다면
                if next_place in snake.keys():
                    # 다음 위치는 뱀 타고 이동한 곳
                    next_place = snake[next_place]
                
                # 이동할 위치에 아무 것도 없고 방문하지 않았다면
                if not visited[next_place]:
                    visited[next_place] = True
                    dice_cnt[next_place] = dice_cnt[x] + 1 # 주사위 굴린 횟수 증가
                    queue.append(next_place)
bfs(1)