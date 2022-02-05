import sys
n = int(sys.stdin.readline())
c_list = [0] * 10001

for i in range(n):
  num = int(sys.stdin.readline())
  
  c_list[num]+=1

for i in range(10001):
  if c_list[i] != 0:
    for j in range(c_list[i]):
      print(i) # 답


# 0으로 되어있는 리스트를 생성하고, 입력 받은 값을 index로 해서 그 index의 값을 +1씩 해줌
# 반복문을 돌면서 0이 아닐 경우 해당 개수만큼 프린트를 해줌