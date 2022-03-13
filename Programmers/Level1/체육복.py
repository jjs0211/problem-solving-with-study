def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in reserve:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    answer = n - len(lost)

    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1

    return answer # 2개 틀림