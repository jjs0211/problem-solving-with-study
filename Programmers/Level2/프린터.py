def solution(priorities, location):
    cnt = 0
    while True:
        max_p = max(priorities)
        first = priorities[0]
        del priorities[0]
        location -= 1
        
        if max_p == first:
            cnt += 1
            if location < 0: # 위에서 제일 첫번째 애들을 뽑을 때 마다 1을 빼주므로 location이 0보다 작다는건 내가 요청한 문서를 뽑았다는 의미
                return cnt
        else:
            priorities.append(first)
            if location < 0:
                location = len(priorities)-1