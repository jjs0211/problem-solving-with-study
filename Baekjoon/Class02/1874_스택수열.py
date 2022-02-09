n = int(input())
cnt = 1
stack = []
result = []
temp = True
for _ in range(n):
    num = int(input())
    while cnt<=num:
        stack.append(cnt)
        cnt += 1  # 1부터 num까지 stack 만들어 주기
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-') # pop
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in result:
        print(i)