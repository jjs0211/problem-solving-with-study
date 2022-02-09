from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = deque(list(map(int, input().split())))
    cnt = 0

    while True:
        first = max(priority) # 제일 첫 번째로 출력할 문서
        front = priority.popleft() # 가장 앞에 있는 문서를 뽑음
        m-=1 # 내 위치가 한 칸 당겨짐

        if first == front: # 뽑은 문서의 우선 순위가 가장 클 때
            cnt+=1 # 순번을 +1
            if m < 0: # m이 0이라는 것은 내 차례라는 뜻이므로 그 때의 순번을 출력
                print(cnt)
                break
        else: # 뽑은 문서의 우선 순위가 가장 큰 게 아니면
            priority.append(front) # 뽑은 문서를 가장 뒤로 보냄
            if m < 0: # 만약 내 문서가 가장 앞에서 뽑히면
                m = len(priority)-1 # 제일 뒤로 보내기