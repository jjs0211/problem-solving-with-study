l = int(input())
str = input()

result = 0
dict={}

for i in range(1, 27):
  dict[chr(i+96)] = i

for i in range(len(str)):
  if str[i] in dict:
    result += dict[str[i]]*(31**i)
print(result%1234567891)

# math.powe 하면 소수점 나옴
# math.trunc(), int()로 소수점 버릴 수 있음