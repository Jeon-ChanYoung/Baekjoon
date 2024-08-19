from collections import deque

R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())
board = [[True]*9 for _ in range(10)]
board[R2][C2] = False
visit = [[False]*9 for _ in range(10)]
visit[R1][C1] = True
Q = deque([(C1, R1, 0)])

while Q:
    x,y,count = Q.popleft()
    if x==C2 and y==R2:
        print(count)
        break

    for dx,dy in [(-3,2),(-3,-2),(-2,3),(-2,-3),(2,3),(2,-3),(3,2),(3,-2)]:
        X = x+dx
        Y = y+dy
        if 0<=X<9 and 0<=Y<10 and not visit[Y][X]:
            if (dx,dy) == (-3,2) and board[y][x-1] and board[y+1][x-2] or \
               (dx,dy) == (-3,-2) and board[y][x-1] and board[y-1][x-2] or \
               (dx,dy) == (-2,3) and board[y+1][x] and board[y+2][x-1] or \
               (dx,dy) == (-2,-3) and board[y-1][x] and board[y-2][x-1] or \
               (dx,dy) == (2,3) and board[y+1][x] and board[y+2][x+1] or \
               (dx,dy) == (2,-3) and board[y-1][x] and board[y-2][x+1] or \
               (dx,dy) == (3,2) and board[y][x+1] and board[y+1][x+2] or \
               (dx,dy) == (3,-2) and board[y][x+1] and board[y-1][x+2]:
               visit[Y][X] = True
               Q.append((X,Y,count+1))