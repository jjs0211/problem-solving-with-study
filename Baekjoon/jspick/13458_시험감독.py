n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for i in a:
    if i<=b: # 한 반에 들어 있는 학생이 총 감독관이 감시할 수 있는 수 보다 적은 경우에는 총 감독관 한명만 필요
        result += 1
    else: 
        i -= b # 그게 아니면 한 반의 학생 수에서 총 감독관 감시 학생 수 빼주고 결과 +1
        result += 1

        if i < c: # 만약 남은 학생 수가 보조 감독관이 감시할 수 있는 학생 수보다 적다면 보조 감독관 한명만 필요하므로 +1
            result += 1
        else: # 그게 아니면
            if i%c == 0: # 만약 남은 학생 수가 보조 감독관 감시 학생 수로 나누어 떨어지면
                result += i//c # 결과 + 몫
            else:# 그게 아니면
                result += i//c + 1 # 결과 + 몫 + 1
print(result)