import sys
import math
n = int(sys.stdin.readline())
fac = math.factorial(n)
cnt = 0
for i in str(fac)[::-1]:
    if int(i) == 0:
        cnt+=1
        continue
    else:
        print(cnt)
        break
