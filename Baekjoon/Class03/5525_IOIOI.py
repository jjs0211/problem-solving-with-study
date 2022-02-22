# import sys
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# s = sys.stdin.readline()
# cnt = 0
# p = [0, 'IOI', 'IOIOI', 'IOIOIOI']
# for i in range(4, n+1):
#     p.append(p[i-1] + 'OI')

# for i in range(m-len(p[n])+1):
#     if p[n] == s[i:i+len(p[n])]:
#         cnt += 1
# print(cnt) # 50점

