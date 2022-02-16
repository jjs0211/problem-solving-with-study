# import sys
# t = int(sys.stdin.readline())

# def fibo(n):
#     if n == 0:
#         return [1, 0]
#     elif n == 1:
#         return [0, 1]
#     else:
#         return fibo(n-1) + fibo(n-2)

# odd = 0
# even = 0
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     for i in range(len(fibo(n))):
#         if i % 2 ==0: # 컴퓨터 인덱스에서는 홀수
#             odd +=fibo(n)[i]
#         else:
#             even +=fibo(n)[i]
# print(odd, even) ## 시간초과

import sys
t = int(sys.stdin.readline())

for _ in range(t):
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    n = int(sys.stdin.readline())
    if n >1: # n이 0과 1일때는 이미 있으므로
        for i in range(n-1): # index가 0부터 시작하니까 n = 4일때 3개만 더 추가되면 되니까
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2]+cnt_1[-1]) # 위에서 0의 수를 추가해줬기 때문에 이전 단계에서의 0의 개수는 [-2]가 됨
    print(cnt_0[n], cnt_1[n])

## 0의 개수 = 이전 단계에서의 1의 개수
## 1의 개수 = 이전 단계에서의 0의 개수 + 이전 단계에서의 1의 개수


# f(2) = 1,1
# f(3) = 1,2
# f(4) = 2,3
# f(5) = 3,5
# f(6) = 5,8
# f(7) = 8,13