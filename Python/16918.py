from copy import deepcopy

def nearby_install():
    pos = set()
    for y in range(R):
        for x in range(C):
            if board[y][x] == "O":
                pos.add((x,y))
            else:
                board[y][x] = "O"
    return pos

def boom():
    global board
    new_board = deepcopy(board)

    for y in range(R):
        for x in range(C):
            if (x,y) in pos:
                new_board[y][x] = "."
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    X = x+dx
                    Y = y+dy
                    if 0<=X<C and 0<=Y<R:
                        new_board[Y][X] = "."
    board = new_board

R,C,N = map(int, input().split())
board = [list(input()) for _ in range(R)]
time = 0

for time in range(1, N):
    if time%2 != 0:
        pos = nearby_install()
    else:
        boom()

for i in board:
    print("".join(i))