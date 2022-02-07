n = int(input())
cnt = 0
six_n = 666
while True:
  if '666' in str(six_n):
      cnt += 1
  if cnt == n:
      print(six_n)
      break
  six_n += 1

  # 666에서 1씩 증가시키면서 만약에 666을 포함하고 있는 숫자들 중 몇번째 숫자인지 확인할 수 있도록 cnt를 +1 해주기