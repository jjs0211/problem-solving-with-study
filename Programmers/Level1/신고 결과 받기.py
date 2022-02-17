def solution(id_list, report, k):
    report = set(report) # 한 사람이 같은 사람에게 신고 여러번 한 경우는 한 번만 쳐주므로 set으로 중복 제거
    report = list(report)
    reporter = []
    reported = []
    idx_reported=[]
    result = {}
    for i in report:
        reporter.append(i.split()[0]) # 신고자 리스트
        reported.append(i.split()[1]) # 피신고자 리스트
    set_reported = set(reported)
    set_reported = list(set_reported) # 피신고자 count 편하게 세기 위해 중복을 지운 리스트를 하나 만듦
    for j in range(len(set_reported)):
        if reported.count(set_reported[j]) >= k: # 신고를 k번 이상 당했다면
            idx_reported.extend(list(filter(lambda x: reported[x] == set_reported[j], range(len(reported))))) # 피신고자 리스트에서 중복되는 값들의 index를 모두 받아옴(신고자 리스트와 피신고자 리스트의 index가 같으니까)
            # x = [0, 1, 2, 3, 4] 에서 reported[x] == set_reported[j] 즉, k번 이상 신고당한 사람의 인덱스를 뽑아옴
    for k in idx_reported:
        if reporter[k] not in result:
            result[reporter[k]] = 1
        else:
            result[reporter[k]]+=1
    print(reporter)
    print(reported)
    print(result) # result에는 신고자가 몇 번 신고했는지 나옴
    real_result = []
    for x in id_list:
        if x in result:
            real_result.append(result[x])
        else:
            real_result.append(0)
    print(real_result)

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)



# def solution(id_list, report, k):
#     users = {name:[] for i, name in enumerate(id_list)}
#     ban_users = {name:0  for i, name in enumerate(id_list)}
#     # print(users)
#     # print(ban_users)
    
#     for temp in set(report):
#         user, ban_user = temp.split(" ")
#         users[user].append(ban_user)
#         ban_users[ban_user] += 1
    
#     # print(users)
#     # print(ban_users)
    
#     answer = [0 for _ in range(len(id_list)) ]
#     print(answer)
#     for key, values in users.items():
#         for value in values:
#             if ban_users[value] >= k:
#                 answer[id_list.index(key)] += 1
#     # print(answer)
    
#     return answer