n = int(input())

student_list = []
for _ in range(n):
    student_list.append(input())

for i in range(1, len(student_list[0])+1):
    check = []
    for j in range(len(student_list)):
        if student_list[j][-i:] in check:
            break
        else:
            check.append(student_list[j][-i:])
    if len(check) == n:
        print(i)
        break