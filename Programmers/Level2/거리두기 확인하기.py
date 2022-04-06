from collections import deque

def solution(places):
    result = []

    def bfs(x, y):
        distance = 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()
        queue.append((x, y))
        visited = [[False]*5 for _ in range(5)]

        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if visited[nx][ny]: # 원래 왔던 곳을 한 번 더 방문하면 안되니까
                    continue
                if waiting_room[nx][ny] == 'X': # 파티션이 있으면 무시
                    continue
                if waiting_room[nx][ny] == 'P': # 거리가 2이하일 때 다른 사람이 발견되면 바로 false 리턴
                    return False
                if waiting_room[nx][ny] == 'O': # 거리가 2 이하일 때 빈 책상이라면 그 칸으로 가서 그 주변 칸들을 검사해야 하므로 queue에 넣어줌
                    queue.append((nx, ny))
            distance += 1 # 이동이 한 번 끝나게 되면 거리 + 1
            if distance == 3: # 만약 거리가 3이 되었는데 이때까지 false를 리턴하지 않았다면 거리두기를 잘 한 것이므로 True 리턴
                return True
        return True # ?????
            

    for waiting_room in places:
        chk = 0
        for i in range(5):
            for j in range(5):
                if waiting_room[i][j] == 'P':
                    if not bfs(i, j): # 만약 false를 리턴했다면(거리두기를 지키지 못했다면)
                        result.append(0) # result에 0을 추가하고
                        chk = 1 # check를 1로 변경(반복문을 모두 탈출하기 위한 변수(?))
                        break
            if chk: # 두번째 반복문을 탈출하고나서 check가 1이라면
                break # 탈출
        else:
            result.append(1) # for문이 break되지 않고 끝까지 수행되었다면(거리두기를 잘 지켰다면) result에 1추가

    return result