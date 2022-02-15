import sys
n = int(sys.stdin.readline())
c_list = [0] * 10001

for i in range(n):
  num = int(sys.stdin.readline())
  
  c_list[num]+=1

for i in range(10001):
  if c_list[i] != 0:
    for j in range(c_list[i]):
      print(i) # 답