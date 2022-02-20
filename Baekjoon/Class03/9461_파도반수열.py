import sys
t = int(sys.stdin.readline())
ans = [0, 1, 1, 1, 2, 2, 3]
for i in range(7, 101):
    ans.append(ans[i-1]+ans[i-5])
for _ in range(t):
    num = int(sys.stdin.readline())
    print(ans[num])

# 1 1 1 2 2 3 4 5 7 9 12 16 21 28 ...