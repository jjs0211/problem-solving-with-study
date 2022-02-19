def solution(new_id):
    result = ''
    # lv1
    new_id = new_id.lower()

    # lv2
    for i in new_id:
        if i.isalnum() == True or i in ['-', '_', '.']:
            result += i

    # lv3
    while '..' in result:
        result = result.replace('..', '.')

    # lv4
    if result[0] == '.':
        if len(result) >=2:
            result = result[1:]
        else:
            result = '.'
    if result[-1] == '.':
        result = result[:-1]

    # lv5
    if len(result) == 0:
        result += 'a'

    # lv 6
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:14]

    # lv 7
    if len(result) <= 2:
        while True:
            result += result[-1]
            if len(result) > 2:
                break
    return result