# x, y, w, h = map(int, input().split())

# print(min(x,y,abs(x-w),abs(y-h))) // 1085 직사각형에서 탈출


# while True:
#   a = list(map(int, input().split()))
#   if a[0] == 0:
#     break
#   else:
#     a.sort()
#     if a[2]**2 == a[0]**2 + a[1]**2:
#       print("right")
#     else:
#       print("wrong") // 4153 직각삼각형


# t = int(input())
# for _ in range(t):
#   h, w, n = map(int, input().split())
#   floor = n%h
#   room = n//h +1
#   if floor == 0:
#     if room-1 < 10:
#       print("{0}0{1}".format(h, room-1))
#     else:
#       print("{0}{1}".format(h, room-1))
#   else:
#     if room < 10:
#       print("{0}0{1}".format(floor,room))
#     else:
#       print("{0}{1}".format(floor,room)) // 10250 ACM호텔


# n = int(input())
# result = []
# for i in range(1, n+1):
#   creator = n-i
#   c_sum = 0
#   for j in range(len(str(creator))):
#     c_sum += int(str(creator)[j])
#   if n == creator + c_sum:
#     result.append(creator)
# if len(result)!=0:
#   print(min(result))
# else:
#   print(0) //2231 분해합


# n = int(input())
# cnt = [1]

# for i in range(n):
#   cnt.append((i+1)*6)
#   if n == 1:
#     print(1)
#   else:
#     if n<=sum(cnt):
#       print(i+2)
#       break // 2292 벌집


