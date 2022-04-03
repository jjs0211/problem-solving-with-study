def solution(record):
    userInfo = {}
    result = []
    answer = []
    for i in record:
        status = i.split()[0]
        uid = i.split()[1]
        if status != 'Leave':
            name = i.split()[2]
            userInfo[uid] = name
        result.append((status, uid))
    
    for a in result:
        status, uid = a[0], a[1]
        if status == 'Enter':
            answer.append('{0}님이 들어왔습니다.'.format(userInfo[uid]))
        elif status == 'Leave':
            answer.append('{0}님이 나갔습니다.'.format(userInfo[uid]))
    return answer
            