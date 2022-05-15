def solution(id_list, report, k):
    users = {name:[] for name in id_list}
    ban_cnt = {name:0 for name in id_list}
    # print(users)
    # print(ban_cnt)
    
    report = set(report)
    for i in range(len(report)):
        user, ban = report[i].split()
        users[user].append(ban)
        ban_cnt[ban] += 1
    # print(users)
    # print(ban_cnt)

    answer = [0 for _ in range(len(id_list))]
    # print(answer)
    for key, value in users.items():
        for v in value:
            if ban_cnt[v] >= k:
                answer[id_list.index(key)] +=1
    return answer