def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        i, j, k = commands[x][0], commands[x][1], commands[x][2]
        re_array = array[i-1:j]
        answer.append(sorted(re_array)[k-1])
    return answer