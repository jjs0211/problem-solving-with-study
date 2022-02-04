n = int(input())
info = []
for _ in range(n):
  age, name = input().split()
  age = int(age)
  info.append((age,name))

sorted_info = sorted(info, key= lambda x: x[0])
for i in range(len(sorted_info)):
  print(sorted_info[i][0], sorted_info[i][1]) # 4276ms