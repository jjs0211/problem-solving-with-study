def solution(arr1, arr2):
    answer = []
    result = 0
    for i in range(len(arr1)):
        result_list = []
        for j in range(len(arr2[0])):
            result = 0
            for k in range(len(arr1[0])):
                result += arr1[i][k] * arr2[k][j]
            result_list.append(result)
        answer.append(result_list)
    return answer