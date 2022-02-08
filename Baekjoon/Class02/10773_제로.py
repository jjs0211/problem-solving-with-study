import sys
k = int(sys.stdin.readline())
money_list = []
for _ in range(k):
  money = int(sys.stdin.readline())
  
  if money != 0:
    money_list.append(money)
  else:
    money_list.pop()
print(sum(money_list))