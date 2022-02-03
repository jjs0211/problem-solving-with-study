n = int(input())
words_list = []
for _ in range(n):
  words = input()
  words_list.append(words)
words_list = list(set(words_list))
result = sorted(words_list, key = lambda word: (len(word), word))

for i in result:
  print(i) # 시간 오래 걸림