from collections import deque

N,M = map(int, input().split())
X,Y = map(int, input().split())
board = [[0]*N for _ in range(N)]
Q = deque([(Y-1, X-1)])

while Q:
    x,y = Q.popleft()

    for X,Y in [(x-2,y-1), (x-2,y+1), (x-1,y-2), (x-1,y+2), (x+1,y-2), (x+1,y+2), (x+2,y-1), (x+2,y+1)]:
        if 0<=X<N and 0<=Y<N and board[Y][X] == 0:
            board[Y][X] = board[y][x] + 1
            Q.append((X,Y))
answer=[]
for _ in range(M):
    A,B = map(int, input().split())
    answer.append(board[A-1][B-1])
print(*answer)