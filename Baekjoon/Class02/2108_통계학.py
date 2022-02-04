n = int(input())
num_list = []
for _ in range(n):
  num = int(input())
  num_list.append(num)

sorted_num_list = sorted(num_list)

print(round(sum(num_list)/len(num_list))) # 평균
print(sorted_num_list[len(num_list)//2]) # 중앙값

# num_dict = {}
# for i in sorted_num_list:
#   if i not in num_dict:
#     num_dict[i] = 1
#   else:
#     num_dict[i] += 1

# print(num_dict)
num_count_list = []
for i in sorted_num_list:
  num_count_list.append(sorted_num_list.count(i))

if num_count_list.count(max(num_count_list)) >= 2:
  print(sorted_num_list[num_count_list.index(max(num_count_list))])
  
else:
  print(sorted_num_list[1])


print(max(num_list) - min(num_list)) # 범위
