from collections import deque

N,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S,I,J = map(int, input().split())

temp = []
for y in range(N):
    for x in range(N):
        if board[y][x] != 0:
            temp.append((board[y][x],x,y,0))
Q = deque(sorted(temp))

while Q:
    num, x, y, time = Q.popleft()
    if time == S:
        continue
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        X = x+dx
        Y = y+dy
        if 0<=X<N and 0<=Y<N and board[Y][X] == 0:
            board[Y][X] = num
            Q.append((num, X, Y, time+1))
print(board[I-1][J-1])