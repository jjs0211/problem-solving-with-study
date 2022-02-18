# import sys
# n, m = map(int, sys.stdin.readline().split())
# num_list = list(map(int, sys.stdin.readline().split()))
# for _ in range(m):
#     start, end = map(int, sys.stdin.readline().split())
#     print(sum(num_list[start-1:end])) 시간초과

# @@@@@@@@@ 구간합 알고리즘@@@@@@@@
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]    # index 계산 편하게 하기 위해 0을 넣어놓음
 
temp = 0    
for i in arr:    # 
    temp += i
    prefix_sum.append(temp) # 각 합들을 추가
 
for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])
