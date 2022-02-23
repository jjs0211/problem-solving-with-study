# def solution(numbers, hand):
#     result = ''
#     l_current = '*'
#     r_current = '#'
#     numbers = [str(i) for i in numbers]
#     pad = {'1':[0,0], '2':[0,1], '3':[0,2],
#            '4':[1,0], '5':[1,1], '6':[1,2],
#            '7':[2,0], '8':[2,1], '9':[2,2],
#            '*':[3,0], '0':[3,1], '#':[3,2]}
#     for i in numbers:
#         if i in ['1', '4', '7', '*']:
#             result += 'L'
#             l_current = i
#         elif i in ['3', '6', '9', '#']:
#             result += 'R'
#             r_current = i
#         elif i in ['2', '5', '8', '0']:
#             if abs(pad[l_current][0]-pad[i][0]) + abs(pad[l_current][1] - pad[i][1]) < abs(pad[r_current][0]-pad[i][0]) + abs(pad[r_current][1] - pad[i][1]):
#                 result += 'L'
#                 l_current = i
#             elif abs(pad[l_current][0]-pad[i][0]) + abs(pad[l_current][1] - pad[i][1]) > abs(pad[r_current][0]-pad[i][0]) + abs(pad[r_current][1] - pad[i][1]):
#                 result += 'R'
#                 r_current = i
#             else:
#                 if hand == 'right':
#                     result += 'R'
#                     r_current = i
#                 else:
#                     result += 'L'
#                     l_current = i


def solution(numbers, hand):
    result = ''
    l_current = '*'
    r_current = '#'
    numbers = [str(i) for i in numbers]
    pad = {'1':[0,0], '2':[0,1], '3':[0,2],
           '4':[1,0], '5':[1,1], '6':[1,2],
           '7':[2,0], '8':[2,1], '9':[2,2],
           '*':[3,0], '0':[3,1], '#':[3,2]}
    
    for i in numbers:
        if i in ['1', '4', '7', '*']:
            result += 'L'
            l_current = i
        elif i in ['3', '6', '9', '#']:
            result += 'R'
            r_current = i
        elif i in ['2', '5', '8', '0']:
            curPos = pad[i]
            lPos = pad[l_current]
            rPos = pad[r_current]
            ldist = abs(curPos[0] - lPos[0]) + abs(curPos[1] - lPos[1])
            rdist = abs(curPos[0] - rPos[0]) + abs(curPos[1] - rPos[1])

            if ldist < rdist:
                result += 'L'
                l_current = i
            elif ldist > rdist:
                result += 'R'
                r_current = i
            else:
                if hand == 'right':
                    result += 'R'
                    r_current = i
                else:
                    result += 'L'
                    l_current = i
    return result