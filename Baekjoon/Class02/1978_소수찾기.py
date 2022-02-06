import sys
n = int(sys.stdin.readline())
num = list(map(int, input().split()))
cnt = 0

for i in num:
  if i == 1: # 1은 소수가 아니므로 pass
    pass
  else:
    for j in range(2, i): # 2부터 입력받은 수까지
      if i % j == 0: # 입력받은 수가 j로 나눠진다면 소수가 아니므로 지금 반복문 탈출
        break
    else: # 아니라면 소수이므로 cnt+1
      cnt+=1
print(cnt) # 답