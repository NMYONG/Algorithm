T = int(input())

for tc in range(1, T+1):
    lst = input().split()

    N = int(lst[0])

    pos = {'B': 1, 'O': 1}

    robot, x = lst[1], int(lst[2])

    pre_robot = robot
    pre_time = x
    pos[robot] = x
    total = x

    for i in range(3, len(lst), 2):
        robot, x = lst[i], int(lst[i+1])
        if pre_robot == robot:
            time = abs(x-pos[robot]) + 1
            total += time

            pre_time += time
            pre_robot = robot
            pos[robot] = x
        else:
            time = abs(x-pos[robot])
            if time < pre_time:
                time = 1
            else:
                time = time - pre_time + 1
            pre_time = time