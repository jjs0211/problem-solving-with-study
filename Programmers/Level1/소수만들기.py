from itertools import combinations
def solution(nums):
    a = list(combinations(nums, 3))
    cnt = 0

    for i in a:
        for j in range(2, int(sum(i)**0.5)+1):
            if sum(i)%j == 0:
                break
        else:
            cnt+=1
    return cnt