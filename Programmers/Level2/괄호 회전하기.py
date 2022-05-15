def solution(s):
    x = len(s)
    cnt = 0
    for i in range(x):
        if i == 0:
            s = s
        else:
            s = s[1:]+s[:1]
        
        check = []
        if s.startswith(")") or s.startswith("]") or s.startswith("}"):
            continue
        else:
            for i in s:
                if i in ['(', '[', '{']:
                    check.append(i)
                elif i == ')':
                    if len(check) != 0 and check[-1] == '(':
                        check.pop()
                elif i == ']':
                    if len(check) != 0 and check[-1] == '[':
                        check.pop()
                else:
                    if len(check) != 0 and check[-1] == '{':
                        check.pop()

        if len(check)==0:
            cnt += 1
    return cnt