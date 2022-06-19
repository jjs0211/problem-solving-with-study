def solution(s):
    zero_cnt = 0
    cnt = 0
    while True:
        check = ''
        for i in s:
            if i != '0':
                check += i
        zero_cnt += len(s) - len(check)
        check = format(len(check), 'b')

        s = check
        cnt += 1
        if len(s) == 1:
            break
    return [cnt, zero_cnt]