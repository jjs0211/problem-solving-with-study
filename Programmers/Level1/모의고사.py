def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]

    cnt = [0, 0, 0]

    for i in range(len(answers)):
        s1 = i%5
        s2 = i%8
        s3 = i%10

        if answers[i] == supo1[s1]:
            cnt[0] +=1
        if answers[i] == supo2[s2]:
            cnt[1] +=1
        if answers[i] == supo3[s3]:
            cnt[2] +=1

    gosu = max(cnt)
    result = []

    for i, val in enumerate(cnt):
        if val == gosu:
            result.append(i+1)
    return result