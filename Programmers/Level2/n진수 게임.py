def jinsoo(n, number):
    js = ''
    dict = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    if number < n:
        if number%n >= 10:
            return dict[str(number%n)]
        else:
            return str(number)
    else:
        while number > 0:
            js += str(number%n)
            number = number//n
        js = js[::-1]
        return js

def solution(n, t, m, p):
    number = t * m

    j = ''
    for i in range(number+1):
        j+=jinsoo(n, i)
    # print(j)
    result = ''
    cnt = 0
    for i in range(p-1, len(j), m):
        if cnt == t:
            break
        else:
            result += j[i]
            cnt += 1
    return result