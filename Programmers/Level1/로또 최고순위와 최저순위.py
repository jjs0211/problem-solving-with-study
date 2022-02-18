def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    correct = 0
    answer = []
    for i in lottos:
        for j in win_nums:
            if i == j:
                correct+=1
    high = correct + zero_cnt
    low = correct

    if high == 6:
        answer.append(1)
    elif high == 5:
        answer.append(2)
    elif high == 4:
        answer.append(3)
    elif high == 3:
        answer.append(4)
    elif high == 2:
        answer.append(5)
    else:
        answer.append(6)

    if low == 6:
        answer.append(1)
    elif low == 5:
        answer.append(2)
    elif low == 4:
        answer.append(3)
    elif low == 3:
        answer.append(4)
    elif low == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer