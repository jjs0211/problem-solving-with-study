def solution(n,a,b):
    cnt = 1
    while True:
        if a%2!=0 and b-a == 1: # a가 더 작을 때
            break
        elif b%2!=0 and a-b == 1: # b가 더 작을 때
            break
        else:
            if a % 2 == 0:
                a//=2
            else:
                a = a//2 + 1
            if b % 2 == 0:
                b//=2
            else:
                b = b//2+1
            cnt += 1
        
    return cnt
        