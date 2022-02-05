from collections import Counter
import sys

n = int(sys.stdin.readline())
num_list = []
for _ in range(n):
  num = int(sys.stdin.readline())
  num_list.append(num)

sorted_num_list = sorted(num_list)

print(round(sum(num_list)/n)) # 평균
print(sorted_num_list[len(num_list)//2]) # 중앙값

c_num_list = Counter(sorted_num_list).most_common()
if len(c_num_list) >1:
  if c_num_list[0][1] == c_num_list[1][1]:
    print(c_num_list[1][0])
  else:
    print(c_num_list[0][0])
else:
  print(c_num_list[0][0])


# print(sorted_num_list[-1] - sorted_num_list[0]) # 범위


# Counter().most_common(숫자)
# 빈도수가 높은 값을 숫자만큼 가져옴(튜플 형태로)

# from collections import Counter
# ls = [1,1,2,3,4,5,5,6,7,8]
# c_ls = Counter(ls).most_common(2) // [(1,2), (5,2)]