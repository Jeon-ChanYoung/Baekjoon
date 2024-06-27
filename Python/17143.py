def catching(x):
    global count
    for y in range(R):
        num = board[y][x]
        if num != 0:
            board[y][x] = 0
            size = shark_info[num][4]
            count += size
            return
        
def movingSharks():
    global board
    new_board = [[0]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if board[y][x] != 0:
                moving(board[y][x], new_board)
    board = [row[:] for row in new_board]  # 깊은 복사

def moving(num, new_board):
    y,x,s,d,z = shark_info[num]
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽

    for _ in range(s):
        dx,dy = directions[d-1]
        x += dx
        y += dy
        x,y,d = AdjustingBorder(x,y,d)

    shark_info[num] = [y, x, s, d, z]  # 상어의 위치와 방향 업데이트
    if new_board[y][x] == 0 or shark_info[new_board[y][x]][4] < z:
        new_board[y][x] = num
        
def AdjustingBorder(x, y, d):
    if y < 0:
        return x, y + 2, 2
    if y >= R:
        return x, y - 2, 1
    if x < 0:
        return x + 2, y, 3
    if x >= C:
        return x - 2, y, 4
    return x, y, d

R,C,M = map(int, input().split())
shark_info = [[0,0,0,0,0]] + [list(map(int, input().split())) for _ in range(M)]
board = [[0]*C for _ in range(R)]
count = 0

for shark in shark_info[1:]:
    shark[0] -= 1
    shark[1] -= 1

for num in range(1, M+1):
    r,c,_,_,_ = shark_info[num]
    board[r][c] = num

# 낚시 시작
for x in range(C):
    catching(x)
    movingSharks()

print(count)

