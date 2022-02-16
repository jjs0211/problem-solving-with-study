# import sys
# n, m =map(int, sys.stdin.readline().split())
# dogam = {}
# cnt = 1
# for _ in range(n):
#     pkm = sys.stdin.readline().rstrip()
#     if pkm not in dogam:
#         dogam[pkm] = cnt
#     cnt+=1
# for _ in range(m):
#     quiz = sys.stdin.readline().rstrip()
#     if quiz.isdigit():
#         quiz = int(quiz)
#         for key, value in dogam.items():
#             if value == quiz:
#                 print(key)
#     else:
#         print(dogam[quiz])  ## 시간초과

import sys
n, m =map(int, sys.stdin.readline().split())
dogam = {}
cnt = 1
for i in range(1, n+1):
    pkm = sys.stdin.readline().rstrip()
    dogam[i] = pkm
    dogam[pkm] = i
for i in range(m):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isdigit(): # 숫자형태의 문자열이면 true 반환
        print(dogam[int(quiz)])
    else:
        print(dogam[quiz])