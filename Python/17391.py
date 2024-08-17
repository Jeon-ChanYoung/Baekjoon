from collections import deque

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
Q = deque([(0, 0, board[0][0], 0)]) # x, y, booster, count


while Q:
    x, y, booster, count = Q.popleft()
    if x==M-1 and y==N-1:
        print(count)
        break
    
    for i in range(1, booster+1):
        X = x+i
        Y = y+i
        if 0<=X<M and not visit[y][X]:
            visit[y][X] = True
            Q.append((X, y, board[y][X], count+1))
        if 0<=Y<N and not visit[Y][x]:
            visit[Y][x] = True
            Q.append((x, Y, board[Y][x], count+1))


