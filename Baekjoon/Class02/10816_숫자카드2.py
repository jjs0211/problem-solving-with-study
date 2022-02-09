import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
m = int(input())
check_list = list(map(int, sys.stdin.readline().split()))
result = []
num_dict = {}

for i in num_list:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] +=1
for j in check_list:
    if j in num_dict:
        print(num_dict[j], end =' ')
    else:
        print(0, end=' ')
