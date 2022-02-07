n = int(input())
info = []
for _ in range(n):
  weight, height = map(int, input().split())
  info.append((weight, height))

for i in info:
  rank = 1
  for j in info:
    if i[0] < j[0] and i[1] < j[1]: # 다 비교하면서 자기보다 몸무게와 키 둘 다 큰 사람이 있으면 랭크 +1
      rank+=1
  print(rank) # 