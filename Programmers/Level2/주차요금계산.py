import math
def solution(fees, records):
    record_dict = {}
    result_dict = {}
    answer = []
    result = []
    for record in records:
        r = record.split(" ")
        r0 = r[0].split(":")
        time = int(r0[0]) * 60 + int(r0[1])

        if r[1] not in record_dict:
            record_dict[r[1]] = time
        else:
            parking_time = abs(time - record_dict[r[1]])
            if r[1] not in result_dict:
                result_dict[r[1]] = parking_time
            else:
                result_dict[r[1]]+=parking_time
            del record_dict[r[1]]


    for i in record_dict:
        if i not in result_dict:
            result_dict[i] = 23*60+59 - record_dict[i]
        else:
            result_dict[i]+=23*60+59 - record_dict[i]
    print(result_dict)
    
    for key, values in result_dict.items():
        fee = 0
        if values <= fees[0]:
            fee += fees[1]
        else:
            p_fee = fees[1] + math.ceil((values - fees[0])/fees[2]) * fees[-1]
            fee += p_fee
        answer.append((key, fee))
    answer = sorted(answer, key = lambda x : x[0])
    for i in answer:
        result.append(i[-1])
    return result