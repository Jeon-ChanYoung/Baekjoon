from collections import deque

graph = [input() for _ in range(10)]
visit = [[False]*10 for _ in range(10)]
Q = deque()

for y in range(10):
    for x in range(10):
        if graph[y][x] == 'B':
            Q.append((x,y,0))
            visit[y][x] = True

while Q:
    x,y,count = Q.popleft()
    if graph[y][x] == "L":
        print(count-1)
        break   

    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        X = x+dx
        Y = y+dy
        if 0<=X<10 and 0<=Y<10 and not visit[Y][X] and graph[Y][X] != "R":
            visit[Y][X] = True
            Q.append((X,Y,count+1))
