import sys
from itertools import product
t = int(sys.stdin.readline())
a = [1,2,3]

for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    for i in range(1, n+1):
        a_list = list(product(a, repeat = i))
        for j in range(len(a_list)):
            if sum(a_list[j]) == n:
                cnt +=1
    print(cnt)