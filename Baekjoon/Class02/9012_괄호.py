n = int(input())

for _ in range(n):
    isVPS = input()
    s_list = []

    for i in isVPS:
        if i == '(':
            s_list.append(i)
        elif i == ')':
            if len(s_list) != 0 and s_list[-1] == '(':
                s_list.pop()
            else:
                s_list.append(i)

    if len(s_list) == 0:
        print('YES')
    else:
        print('NO')