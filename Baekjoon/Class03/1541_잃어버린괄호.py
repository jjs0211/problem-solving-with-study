ex = input().split('-')
print(ex)
num = []
for i in ex: # 55-25+30-13 일 때 ex = ['55', '25+30', '13']
    cnt = 0
    s = i.split('+') # s = ['55'] , ['25', '30'], ['13']
    for j in s:
        cnt+=int(j)
    num.append(cnt) # num = [55, 55, 13]
n = num[0] # 맨 처음 애는 더해줘야하므로
for i in range(1, len(num)):
    n-=num[i] # 입력 받을 때 -를 기준으로 split 했으므로 -해주면 됨
print(n)