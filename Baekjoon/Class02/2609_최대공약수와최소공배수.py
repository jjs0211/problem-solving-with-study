# from sys import stdin
# a, b = map(int, stdin.readline().split())
# max_num = max(a,b)
# min_num = min(a,b)
# # breaker = False

# for i in range(min_num//2, 0, -1):
#   if a%i==0 and b%i==0:
#     print(i)
#     break

# # for i in range(2, min_num+1):
# #   for j in range(i, max_num+1):
# #     if max_num*i == min_num*j:
# #       print(max_num*i)
# #       breaker = True
# #       break
# #     if breaker == True:
# #       break # 시간초과

# for i in range(max_num, a*b+1):
#   if i % max_num == 0 and i % min_num==0:
#     print(i)
#     break

import sys 
A, B = map(int, sys.stdin.readline().split())
a, b = A, B 
while b != 0: 
  a = a % b 
  a, b = b, a 
  
print(a)
print(A*B//a)

# a, b의 최대공약수는 b와 a%b의 최대공약수와 같음(a>b 일 때)
# (24,18) -> (18, 6) -> (6, 0) b가 0이 되는 순간의 6이 최대공약수

# A와 B는 각각 x*gcd(a, b), y*gcd(a, b)이다. 따라서 A*B/gcd(a, b)를 해주면 최소공배수가 된다 (??)


