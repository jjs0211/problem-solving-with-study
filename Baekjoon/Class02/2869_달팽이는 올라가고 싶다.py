a, b, v = map(int, input().split())

cnt = 0
h = 0
while 1:
  cnt +=1
  h = h + a
  if h >= v:
    break
  else:
    h -= b

print(cnt)