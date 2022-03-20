def solution(dartResult):
    dart = {}

    a = ''
    flag = ''
    for i in dartResult:
        if i.isdigit():
            if flag == 's':
                a = ''
            a+=i
            flag = 'n'
        else:
            if flag == 'n':
                if a not in dart:
                    dart[a] = i
                else: # 이 조건이 없다면 10D4S10D와 같은 경우에 {'10' : 'D', '4' : 'S'} 이렇게만 나옴. 조건이 있다면 {'10' : 'DD', '4' : 'S'}
                    dart[a] += i
            else:
                dart[a]+=i
            flag = 's'
    print(dart)

    answer_list = []
    for key, value in dart.items():
        answer = 0
        for i in value:
            if i == 'S':
                answer += int(key)**1
            elif i == 'D':
                answer += int(key)**2
            elif i == 'T':
                answer += int(key)**3
            elif i == '*':
                if len(answer_list) == 0:
                    answer *= 2
                else:
                    answer_list[-1] = answer_list[-1] * 2
                    answer *= 2
            elif i == '#':
                answer = answer*(-1)
        answer_list.append(answer)
    return sum(answer_list)

solution("10D4S10D")

