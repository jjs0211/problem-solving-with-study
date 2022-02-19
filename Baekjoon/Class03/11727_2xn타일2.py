s = [0, 1, 3]
for i in range(3, 1001):
  s.append((s[i - 2] * 2) + s[i - 1])
n = int(input())
print(s[n] % 10007)

# x = 1 : 1
# x = 2 : 3
# x = 3 : 5
# x = 4 : 11

# 5(x:3일때) = x:2일때 + x:1일때*2
# 11(x:4일때) = x:3일때 + x:2일때*2