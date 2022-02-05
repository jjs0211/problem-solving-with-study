# import sys
# n = int(sys.stdin.readline())
# n_ls = [i for i in range(1,n+1)]

# for i in range(n-2):
#   del n_ls[0]
#   n_ls.append(n_ls[0])
#   del n_ls[0]
# print(n_ls[1]) # 시간초과

import sys
n = int(sys.stdin.readline())
if n == 1:
  print(1)
elif n == 2:
  print(2)
elif n == 3:
  print(2)
elif n == 4:
  print(4)
elif n == 5:
  print(2)
elif n == 6:
  print(4)
elif n == 7:
  print(6)
elif n == 8:
  print(8)
else:
  a = 1
  cnt = 0
  while True:
    cnt +=1
    a *=2
    if a >n:
      cnt -=1
      break
  
  if 2**cnt == n:
    print(n)
  else:
    result = n - 2**cnt
    print(2*result)