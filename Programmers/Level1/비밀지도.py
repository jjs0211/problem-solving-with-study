def solution(n, arr1, arr2):
    arr1_re = []
    arr2_re = []
    arr3_re = []

    for i in arr1:
        e = format(i, 'b') # 2진수로 변경
        if len(e) != n: # 9를 2진수로 변경하면 1001이 나오는데, 2진수의 길이가 n과 같아야 하므로 길이가 n과 같지 않다면 while문을 돌면서 앞에 0을 붙여줌
            while True:
                e = '0' + e
                if len(e) == n:
                    arr1_re.append(e)
                    break
        else:
            arr1_re.append(e)
    for i in arr2:
        e = format(i, 'b')
        if len(e) != n:
            while True:
                e = '0' + e
                if len(e) == n:
                    arr2_re.append(e)
                    break
        else:
            arr2_re.append(e)

    
    for i in range(len(arr1_re)):
        arr3 = ''
        for j in range(len(arr1_re[i])):
            if int(arr1_re[i][j]) or int(arr2_re[i][j]): # arr1_re와 arr2_re를 다 돌면서 같은 인덱스에 있는 애들끼리 int로 변환해서 or 연산. 둘 중 하나라도 1이면 arr3에 1을 더해주고 아니라면 0을 더해줌.
                arr3+='1'
            else:
                arr3+='0'
        arr3_re.append(arr3)
    
    
    result_re = []
    for i in range(len(arr3_re)):
        result = ''
        for j in range(len(arr3_re[i])): # arr3_re를 돌면서 1이라면 '#'을 더해주고 아니라면 공백을 더해줌
            if arr3_re[i][j] == '1':
                result += '#'
            else:
                result += ' '
        result_re.append(result)
    return result_re
            