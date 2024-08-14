from collections import deque

n,m = map(int, input().split())
bitmap = [input() for _ in range(n)]
answer = [[0]*m for _ in range(n)]

Q = deque()
for y in range(n):
    for x in range(m):
        if bitmap[y][x] == '1':
            Q.append((x,y))
while Q:
    x,y = Q.popleft()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        X = x+dx
        Y = y+dy
        if 0<=X<m and 0<=Y<n and answer[Y][X] == 0 and bitmap[Y][X] != '1':
            answer[Y][X] = answer[y][x] + 1
            Q.append((X,Y))

for i in answer:
    print(*i)