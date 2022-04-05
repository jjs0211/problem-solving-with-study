import math
def solution(str1, str2):
    s1 = str1.lower()
    s2 = str2.lower()
    s1_list = []
    s2_list = []
    if s1 == s2:
        return 65536
    else:
        for i in range(len(s1)-1):
            s1_list.append(s1[i:i+2])
        for i in range(len(s2)-1):
            s2_list.append(s2[i:i+2])
    
    s1_list_new = []
    s2_list_new = []
    for i in s1_list:
        if i.isalpha():
            s1_list_new.append(i)
    for i in s2_list:
        if i.isalpha():
            s2_list_new.append(i)
    
    print(s1_list_new)
    print(s2_list_new)
    inter = []
    union = []
    s1_inter = s1_list_new.copy()
    s2_inter = s2_list_new.copy()
    for i in s1_list_new:
        if i in s2_inter:
            inter.append(i)
            s1_inter.remove(i)
            s2_inter.remove(i)
    
    # 다중 집합의 합집합
    s1_list_temp = s1_list_new.copy()
    s1_list_result = s1_list_new.copy()
    for i in s2_list_new:
        if i not in s1_list_temp:
            s1_list_result.append(i)
        else:
            s1_list_temp.remove(i)
            
    union = s1_list_result
    print(inter)
    print(union)
    
    
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return math.trunc(len(inter)/len(union) * 65536)