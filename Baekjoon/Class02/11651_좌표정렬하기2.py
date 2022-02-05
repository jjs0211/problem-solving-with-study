import sys
n = int(sys.stdin.readline())
xy_list = []
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  xy_list.append((x,y))

sorted_list = sorted(xy_list, key = lambda x: (x[1], x[0]))
for i in sorted_list:
  print(i[0], i[1])