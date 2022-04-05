import math
def solution(str1, str2):
    if str1 == str2:
        return 65536
    else:
        s1 = lm(str1)
        s2 = lm(str2)
    
    inter = []
    union = []
    s2_inter = s2.copy()
    for i in s1:
        if i in s2_inter:
            inter.append(i)
            s2_inter.remove(i) # remove를 해주지 않으면 [a,a,a,b,b], [a,a,b,b,b]인 경우에 i 가 첫번째 리스트의 3번째 a 일 때에도 교집합에 추가가 됨
    
    # 다중 집합의 합집합
    s1_list_temp = s1.copy()
    s1_list_result = s1.copy()
    for i in s2:
        if i not in s1_list_temp:
            s1_list_result.append(i)
        else:
            s1_list_temp.remove(i)
            
    union = s1_list_result
    print(inter)
    print(union)
    
    if len(inter) == 0 and len(union) == 0: # 두 집합 모두 공집합일 때 교집합과 합집합 모두 공집합이므로 and를 써야함
        return 65536                        # 만약 or로 한다면 교집합이 공집합이고 합집합은 공집합이 아니라도 65536을 return하므로 안됨
    else:                                   # 교집합이 공집합이고 합집합이 공집합이 아닐때는 0을 return해야함
        return math.trunc(len(inter)/len(union) * 65536)

def lm(s):
    s1 = []
    s = s.lower()
    for i in range(len(s)-1):
        if s[i:i+2].isalpha():
            s1.append(s[i:i+2])
    return s1

# https://velog.io/@munang/개념정리-파이썬-다중-집합




# import math
# def solution(str1, str2):
#     s1 = str1.lower()
#     s2 = str2.lower()
#     s1_list = []
#     s2_list = []
#     if s1 == s2:
#         return 65536
#     else:
#         for i in range(len(s1)-1):
#             s1_list.append(s1[i:i+2])
#         for i in range(len(s2)-1):
#             s2_list.append(s2[i:i+2])
    
#     s1_list_new = []
#     s2_list_new = []
#     for i in s1_list:
#         if i.isalpha():
#             s1_list_new.append(i)
#     for i in s2_list:
#         if i.isalpha():
#             s2_list_new.append(i)
    
#     print(s1_list_new)
#     print(s2_list_new)
#     inter = []
#     union = []
#     s2_inter = s2_list_new.copy()

#     for i in s1_list_new:
#         if i in s2_inter:
#             inter.append(i)
#             s2_inter.remove(i) # remove를 해주지 않으면 [a,a,a,b,b], [a,a,b,b,b]인 경우에 i 가 첫번째 리스트의 3번째 a 일 때에도 교집합에 추가가 됨
    
#     # 다중 집합의 합집합
#     s1_list_temp = s1_list_new.copy()
#     s1_list_result = s1_list_new.copy()
#     for i in s2_list_new:
#         if i not in s1_list_temp:
#             s1_list_result.append(i)
#         else:
#             s1_list_temp.remove(i)
            
#     union = s1_list_result
#     print(inter)
#     print(union)
    
    
#     if len(inter) == 0 and len(union) == 0: # 두 집합 모두 공집합일 때 교집합과 합집합 모두 공집합이므로 and를 써야함
#         return 65536                        # 만약 or로 한다면 교집합이 공집합이고 합집합은 공집합이 아니라도 65536을 return하므로 안됨
#     else:                                   # 교집합이 공집합이고 합집합이 공집합이 아닐때는 0을 return해야함
#         return math.trunc(len(inter)/len(union) * 65536)

# # https://velog.io/@munang/개념정리-파이썬-다중-집합