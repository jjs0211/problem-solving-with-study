def solution(n):
    cnt = 0
    for i in range(n//2):
        answer = 0
        for j in range(i+1, n):
            answer += j
            print(answer)
            if answer == n:
                cnt += 1
                break
            elif answer > n:
                break
    return cnt+1