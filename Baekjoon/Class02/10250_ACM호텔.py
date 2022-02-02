t = int(input())
for _ in range(t):
  h, w, n = map(int, input().split())
  floor = n%h
  room = n//h +1
  if floor == 0:
    if room-1 < 10:
      print("{0}0{1}".format(h, room-1))
    else:
      print("{0}{1}".format(h, room-1))
  else:
    if room < 10:
      print("{0}0{1}".format(floor,room))
    else:
      print("{0}{1}".format(floor,room))