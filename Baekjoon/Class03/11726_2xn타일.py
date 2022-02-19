s = [0, 1, 2]
for i in range(3, 1001):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n] % 10007) 

# x= 2 : 2개
# x= 3 : 3개
# x= 4 : 5개
# x= 5 : 8개
# ...