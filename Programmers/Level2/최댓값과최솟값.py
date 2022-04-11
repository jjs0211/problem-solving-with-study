def solution(s):
    result = []
    a = ''
    for i in s:
        if i != " ":
            a += i
        else:
            result.append(int(a))
            a = ''
    else:
        result.append(int(a))

    max_r = max(result)
    min_r = min(result)
    return str(min_r) + " " + str(max_r)