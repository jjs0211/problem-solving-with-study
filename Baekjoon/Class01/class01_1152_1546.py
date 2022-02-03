# str = list(input().split())
# print(len(str)) // 1152 단어의 개수


# arr = []
# for _ in range(9):
#   arr.append(int(input()))
# print(max(arr), arr.index(max(arr))+1) // 2562 최댓값


# a = int(input())
# b = int(input())
# c = int(input())

# mul = a*b*c

# for i in range(10):
#   print(str(mul).count(str(i))) // 2577 숫자의 개수


# t = int(input())

# for _ in range(t):
#   result = ''
#   r, s = input().split()
#   for i in s:
#     result += i * int(r)
#   print(result) // 2675 문자열 반복


# a, b = input().split()
# reversed_a = a[::-1]
# reversed_b = b[::-1]

# print(max(int(reversed_a),int(reversed_b))) // 2908 상수


# num = input().split()
# ascending = ['1','2','3','4','5', '6','7','8']
# descending = ['8','7','6','5','4','3','2','1']

# if num == ascending:
#   print('ascending')
# elif num == descending:
#   print('descending')
# else:
#   print('mixed') // 2920 음계


# n={}
# for _ in range(10):
#   num = int(input())
#   num %=42
#   if num not in n:
#     n[num] = 1
#   else:
#     n[num]+=1
# print(len(n)) // 3052 나머지


# t = int(input())
# for _ in range(t):
#   ox = input()
#   cnt = 0
#   result = 0
#   for i in range(len(ox)):
#     if ox[i] == 'O':
#       cnt +=1
#     else:
#       cnt = 0
#     result += cnt
#   print(result) // 8958 OX퀴즈


# s = input()

# alphabet = list(range(97,123))

# for i in alphabet:
#   print(s.find(chr(i))) // 10809 알파벳 찾기


# n = int(input())
# num = list(map(int,input()))

# print(sum(num)) //11720 숫자의 합


# n = int(input())
# num = int(input())

# num = str(num)
# num = list(num)
# print(sum(int(i) for i in num)) // 숫자의 합 다른 방법


# word = input().upper()
# result = {}

# for i in word:
#   if i not in result:
#     result[i] = 1
#   else:
#     result[i] +=1

# reverse_result = dict(map(reversed,result.items()))

# if list(result.values()).count(max(result.values())) >=2:
#   print("?")
# else:
#   print(reverse_result[max(result.values())]) // 1157 단어공부


# n = int(input())
# score = list(map(int, input().split()))
# score_copy = []
# for i in range(len(score)):
#   score_copy.append(score[i]/max(score)*100)

# print(sum(score_copy)/len(score_copy)) // 1546 평균