# import math
# n, k = map(int, input().split())

# print(math.factorial(n)//(math.factorial(k) * math.factorial(n-k))) // 라이브러리 사용


# n, k = map(int, input().split())
# n_f = 1
# k_f = 1
# n_k_f = 1
# for i in range(1, n+1):
#   n_f *=i

# for i in range(1, k+1):
#   k_f*=i

# for i in range(1, n-k+1):
#   n_k_f *= i

# print(n_f//(k_f*n_k_f)) // for문