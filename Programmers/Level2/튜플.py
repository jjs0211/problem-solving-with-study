def solution(s):
    result = []
    real_result = []
    ss = []
    s_list = []
    a = ''
    for i in s:
        if i.isdigit():
            a += i
        elif i == ',' or i == '}':
            ss.append(a)
            a = ''
    print(ss)
    for i in ss:
        if i != '':
            s_list.append(int(i))
        else:
            result.append(s_list)
            s_list = []
    print(result)
    result.sort(key = lambda x : len(x))
    for i in result:
        for j in i:
            if j not in real_result:
                real_result.append(j)
    return real_result