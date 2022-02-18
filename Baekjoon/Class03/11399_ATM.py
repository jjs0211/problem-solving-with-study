import sys
n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
sorted_time = sorted(time)
result = 0
for i in range(1, len(sorted_time)+1):
    result += sum(sorted_time[:i])
print(result)