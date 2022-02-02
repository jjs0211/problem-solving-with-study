import math
a, b, v = map(int, input().split())

day = (v-b)/(a-b) # 정상에 도달하면 밤에 미끄러지지 않는 것을 고려 day = v/(a-b)라고 하면 정상에 도달해도 밤에 내려와 다음 날 다시 올라가야하는 일이 생김
print(math.ceil(day))

