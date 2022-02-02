import copy
t = int(input())
for _ in range(t):
  k = int(input()) //층
  n = int(input()) //호
  # zero_floor = list(range(1, n+1))
  ls = list(range(1, n+1)) // 0층
  ls_cp = [0 for _ in range(n)] // 0으로 초기화
  for i in range(k):
    for j in range(n):
      if j == 0:
        ls_cp[j] = 1
      else:
        ls_cp[j] = sum(ls[:j+1])
    ls = copy.deepcopy(ls_cp)
  print(ls[n-1])