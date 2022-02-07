# from sys import stdin, stdout
# n = stdin.readline()
# N = set(stdin.readline().split())
# m = stdin.readline()
# M = stdin.readline().split()

# for i in M:
#   if i in N:
#     stdout.write('1\n')
#   else:
#     stdout.write('0\n')

# # 탐색과 확인이 주로 필요하면 set이나 dictionary
# # 순서와 index에 따르 접근이 필요하면 list


import sys

def binary_search(num, targets):
  left = 0
  right = len(num) -1

  while left <= right:
    mid = (left + right) //2
    if targets == num[mid]:
      return 1
    elif targets > num[mid]:
      left = mid+1
    else:
      right = mid -1
  return 0

n = int(input())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

m = int(input())
targets = list(map(int, sys.stdin.readline().split()))

for i in range(m):
  print(binary_search(num, targets[i]))