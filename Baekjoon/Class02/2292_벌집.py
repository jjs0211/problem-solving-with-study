n = int(input())
cnt = [1]

for i in range(n):
  cnt.append((i+1)*6)
  if n == 1:
    print(1)
  else:
    if n<=sum(cnt):
      print(i+2)
      break