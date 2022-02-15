import sys
n, m = map(int, sys.stdin.readline().split())
p_dict = {}
result = []
for _ in range(n+m):
    people = sys.stdin.readline()
    if people not in p_dict:
        p_dict[people] = 1
    else:
        p_dict[people] += 1

for key, value in p_dict.items():
    if value >=2:
        result.append(key)
print(len(result))
for i in sorted(result):
    print(i, end='')