from collections import deque

def converter(x, y, array):
    array = list(array)
    for i in range(3):
        array[i] = list(array[i])

    array[y][x] = BlackWhite[array[y][x]]
    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        X = x+dx
        Y = y+dy
        if 0 <= X < 3 and 0 <= Y < 3:
            array[Y][X] = BlackWhite[array[Y][X]]
    
    for i in range(3):
        array[i] = tuple(array[i])
    array = tuple(array)

    return array

for _ in range(int(input())):
    board = tuple(tuple(input()) for _ in range(3))
    visit = set()
    BlackWhite = {"*":".",
                ".":"*"}

    Q = deque([[((".",".","."),
                (".",".","."),
                (".",".",".")), 0]])
    while Q:
        array, count = Q.popleft()
        if array == board:
            print(count)
            break
        for i in range(3):
            for j in range(3):
                new_board = converter(j, i, array)
                if new_board not in visit:
                    visit.add(new_board)
                    Q.append([new_board, count + 1])
        