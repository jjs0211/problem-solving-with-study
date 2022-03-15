def solution(num):
    cnt = 0
    if num != 1:
        while True:
            if num%2 == 0:
                num //= 2
                cnt+=1
            elif num%2==1:
                num = num*3 + 1
                cnt+=1
            if cnt == 500 and num != 1:
                return -1
                break
            elif num == 1:
                return cnt
                break
    else:
        return 0