for i in range(1, 10, 1):
    for x in range(10, i, -1):
        print('s', end='')
    for s in range(1, i + 1):
        print('x', end = '')
    print()