from itertools import combinations

n ,m = map(int, input().split())
cards = list(map(int, input().split()))

data = list(combinations(cards,3))
result = []
for i in data:
  result.append(abs(sum(i)-m))
print(sum(data[result.index(min(result))]))

