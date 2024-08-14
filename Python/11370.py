from collections import deque

for Input in iter(input, "0 0"):
    W,H = map(int, Input.split())
    Mirkwood = [list(input()) for _ in range(H)]
    visit = [[False]*W for _ in range(H)]
    Q = deque()

    for y in range(H):
        for x in range(W):
            if Mirkwood[y][x] == "S":
                Q.append((x,y))
                visit[y][x] = True

    while Q:
        x,y = Q.popleft()
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            X = x+dx
            Y = y+dy
            if 0<=X<W and 0<=Y<H and Mirkwood[Y][X] == "T" and not visit[Y][X]:
                visit[Y][X] = True
                Mirkwood[Y][X] = "S"
                Q.append((X,Y))

    for line in Mirkwood:
        print("".join(line))