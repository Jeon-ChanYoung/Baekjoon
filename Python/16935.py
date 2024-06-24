from copy import deepcopy

def number_1():
    global array
    temp = []
    for i in range(N-1, -1, -1):
        temp.append(array[i])
    array = deepcopy(temp)

def number_2():
    global array
    temp = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            temp[y][x] = array[y][M-x-1]
    array = deepcopy(temp)        

def number_3():
    global array
    temp = [[0] * N for _ in range(M)]
    for y in range(M):
        for x in range(N):
            temp[y][x] = array[N-x-1][y]
    array = deepcopy(temp)

def number_4():
    global array
    temp = [[0] * N for _ in range(M)]
    for y in range(M):
        for x in range(N):
            temp[y][x] = array[x][M-y-1]
    array = deepcopy(temp)

def number_5():
    global array
    midx = M // 2
    midy = N // 2 
    temp = [[0] * M for _ in range(N)]

    for y in range(midy):
        for x in range(midx):
            temp[y][x] = array[y+midy][x]
            temp[y][x+midx] = array[y][x]
            temp[y+midy][x] = array[y+midy][x+midx]
            temp[y+midy][x+midx] = array[y][x+midx]
    array = deepcopy(temp)

def number_6():
    global array
    midx = M // 2
    midy = N // 2 
    temp = [[0] * M for _ in range(N)]

    for y in range(midy):
        for x in range(midx):
            temp[y][x] = array[y][x+midx]
            temp[y][x+midx] = array[y+midy][x+midx]
            temp[y+midy][x] = array[y][x]
            temp[y+midy][x+midx] = array[y+midy][x]
    array = deepcopy(temp)    

N,M,R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))

for flag in operations:
    N = len(array)
    M = len(array[0])
    if flag == 1:
        number_1()
    elif flag == 2:
        number_2()
    elif flag == 3:
        number_3()
    elif flag == 4:
        number_4()
    elif flag == 5:
        number_5()
    else:
        number_6()

for arr in array:
    print(*arr)
