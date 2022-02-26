# def solution(participant, completion):
#     for i in participant:
#         if i in completion:
#             del completion[completion.index(i)]
#         else:
#             return i  #효율성 x

def solution(participant, completion):
    result = {}
    for i in participant:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    for i in completion:
        result[i] += 1

    for key, value in result.items():
        if value % 2 != 0:
            return key