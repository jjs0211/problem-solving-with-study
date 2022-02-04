import sys
n = int(input())
num_list = []

for _ in range(n):
  num = int(sys.stdin.readline())
  num_list.append(num)

for i in sorted(num_list):
  sys.stdout.write(str(i)+'\n') # 1428ms
  print(i) # 1580ms