def solution(s):
    s_list = [0]
    for i in s:
        if i == s_list[-1]:
            del s_list[-1]
        else:
            s_list.append(i)
    if len(s_list) == 1:
        return 1
    else:
        return 0