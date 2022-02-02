from itertools import combinations

n ,m = map(int, input().split())
cards = list(map(int, input().split()))

data = list(combinations(cards,3))
result = {}
for i in data:
  if sum(i)<=m:
    result[sum(i)] = abs(sum(i)-m)
  else:
    continue
print(min(result, key = result.get)) // 2798 블랙잭