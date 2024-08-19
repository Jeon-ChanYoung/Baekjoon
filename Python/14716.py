import sys;sys.setrecursionlimit(10**6)

def search(x,y):
    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
        X = x+dx
        Y = y+dy
        if 0<=X<N and 0<=Y<M and banner[Y][X] == "1":
            banner[Y][X] = "0"
            search(X,Y)

M,N = map(int, input().split())
banner = [input().split() for _ in range(M)]
count = 0

for y in range(M):
    for x in range(N):
        if banner[y][x] == "1": 
            banner[y][x] = "0"
            count += 1
            search(x,y)
print(count)