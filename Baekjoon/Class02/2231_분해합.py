n = int(input())
result = []
for i in range(1, n+1):
  creator = n-i
  c_sum = 0
  for j in range(len(str(creator))):
    c_sum += int(str(creator)[j])
  if n == creator + c_sum:
    result.append(creator)
if len(result)!=0:
  print(min(result))
else:
  print(0)