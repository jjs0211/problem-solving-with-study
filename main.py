k = int(input())
money_list = []
for _ in range(k):
  money = int(input())
  
  if money != 0:
    money_list.append(money)
  else:
    money_list.pop()
print(sum(money_list))