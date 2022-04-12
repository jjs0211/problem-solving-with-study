def solution(s):
    if s[0].isdigit():
        result = s[0]
    else:
        result = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            result += s[i].upper()
        else:
            result += s[i].lower()
    return result
            