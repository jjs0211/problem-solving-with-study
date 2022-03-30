t = int(input())

for _ in range(t):
    control = input()
    direction = 'y'

    x = 0
    y = 0
    x_list = []
    y_list = []
    cnt = 0 # 1은 위쪽, 2는 왼쪽, 3은 아래쪽, 4는 오른쪽
    for i in control:
        if direction == 'y': # 내가 바라보는 방향이 y 방향이면
            if cnt%4 == 0: # 위쪽을 보고 있다면
                if i == 'F':
                    y += 1
                elif i == 'B':
                    y -= 1
                elif i == 'L':
                    direction = 'x'
                    cnt += 1
                    continue
                elif i == 'R':
                    if cnt == 0: # cnt가 0일 때는 1을 빼면 -1이 되므로 cnt가 0일 때나 4일 때나 같으므로 3으로 바꿔줌
                        cnt = 3
                        direction = 'x'
                        continue
                    else:
                        direction = 'x'
                        cnt -= 1
                        continue
            elif cnt%4 == 2:
                if i == 'F':
                    y -= 1
                elif i == 'B':
                    y += 1
                elif i == 'L':
                    direction = 'x'
                    cnt += 1
                    continue
                elif i == 'R':
                    direction = 'x'
                    cnt -= 1
                    continue
            y_list.append(y)

        elif direction == 'x':
            if cnt%4 ==1:
                if i == 'F':
                    x -= 1
                elif i == 'B':
                    x += 1
                elif i == 'L':
                    direction = 'y'
                    cnt += 1
                    continue
                elif i == 'R':
                    direction = 'y'
                    cnt -= 1
                    continue
            elif cnt%4 == 3:
                if i == 'F':
                    x += 1
                elif i == 'B':
                    x -= 1
                elif i == 'L':
                    direction = 'y'
                    cnt += 1
                    continue
                elif i == 'R':
                    direction = 'y'
                    cnt -= 1
                    continue
            x_list.append(x)

    if not x_list: # y축에만 선이 그어져 x 축에는 선이 없을 때
        x_list.append(0)
    if not y_list:
        y_list.append(0)

    r_x, r_y = 0, 0
    if len(x_list) == 1:
        r_x = abs(max(x_list))
    else:
        if min(x_list) > 0:
            r_x = max(x_list)
        elif max(x_list) < 0:
            r_x = abs(min(x_list))
        else:
            r_x = max(x_list) - min(x_list)

    if len(y_list) == 1:
        r_y = abs(max(y_list))
    else:
        if min(y_list) > 0:
            r_y = max(y_list)
        elif max(y_list) < 0:
            r_y = abs(min(y_list))
        else:
            r_y = max(y_list) - min(y_list)
    
    # print(x_list, y_list)
    print(abs(r_x) * abs(r_y))
