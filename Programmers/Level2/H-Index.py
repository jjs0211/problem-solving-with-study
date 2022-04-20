def solution(citations):
    citations.sort()
    print(citations)
    result = []
    if max(citations) == 0:
        return 0
    else:
        for i in range(max(citations)):
            if len([x for x in citations if x >= i]) >= i:
                result.append(i)
    print(result)

    return max(result)