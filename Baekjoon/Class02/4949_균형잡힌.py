while True:
    s = input()
    if s == '.':
        break
    s_list = []
    for i in range(len(s)):
        if s[i] in ['(', '[']:
            s_list.append(s[i])
        elif s[i] == ')':
            if len(s_list) != 0 and s_list[-1] == '(':
                s_list.pop()
            else:
                s_list.append(')') # s_list에 아무것도 없으면 yes인데 제일 ')'이 제일 처음 나온 경우에 append를 해주지 않으면 s_list 길이가 0이므로 append 해줌
                break
        elif s[i] == ']':
            if len(s_list) != 0 and s_list[-1] == '[':
                s_list.pop()
            else:
                s_list.append(']')
                break
    if len(s_list) == 0:
        print('yes')
    else:
        print('no')