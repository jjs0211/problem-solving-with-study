def solution(N, stages):
    player = len(stages)
    fail_rate = {}
    dict_stages = {i:0 for i in range(N+1)}

    for i in stages:
        if i not in dict_stages:
            dict_stages[i] = 1
        else:
            dict_stages[i] += 1

 
    for i in range(1, N+1):
        if player == 0:
            fail_rate[i] = 0
        else:
            fail_player = dict_stages[i]
            fail_rate[i] = fail_player/player
            player -= fail_player

        
    fail_rate = dict(sorted(fail_rate.items(), key=lambda x:x[-1], reverse=True))

    return list(fail_rate.keys()) # 이 방법이 훨씬 빠름

print(solution(5, [2,2,2,2,2]))

# def solution(N, stages):
#     player = len(stages)
#     stages = sorted(stages)
#     fail_rate = {}
    
#     for i in range(1, N+1):
#         if player == 0:
#             fail_rate[i] = 0
#         else:
#             fail_player = stages.count(i)
#             fail_rate[i] = fail_player/player
#             player -= fail_player
        
#     fail_rate = dict(sorted(fail_rate.items(), key=lambda x:x[-1], reverse=True))
#     return list(fail_rate.keys())