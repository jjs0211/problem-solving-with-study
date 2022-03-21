from collections import deque
import copy
def solution(progresses, speeds):
    toDo = []
    result = []
    for i in progresses:
        toDo.append(100-i)
    print(toDo) # 남은 일의 양
    
    result = deque()
    for i in range(len(toDo)):
        if toDo[i]%speeds[i] == 0:
            bp = toDo[i] // speeds[i]
            result.append(bp)
        else:
            bp = toDo[i] // speeds[i] + 1
            result.append(bp)
    print(result) # 배포가 가능한 날짜 ([5, 10, 1, 1, 20, 1])
    
    cnt = 1
    answer = []
    a = result.popleft()
    while True:
        b = result.popleft()
        if a < b: # 만약 앞의 날보다 더 늦게 끝났다면
            answer.append(cnt)
            a = b # 원래 a는 배포하였으므로 a에 그 다음 배포해야할 것(b)을 넣어줌
            cnt = 1 
        else: # 만약 앞의 날보다 더 일찍 끝났다면
            cnt += 1 # 배포마다 가능한 배포 수 + 1
        if len(result) == 0:
            answer.append(cnt)
            break
    return answer