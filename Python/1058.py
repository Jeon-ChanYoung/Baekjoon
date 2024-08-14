N = int(input())
world = [input() for _ in range(N)]
paths = [[float('inf')]*N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if world[y][x] == "Y":
            paths[y][x] = 1
        elif x==y:
            paths[y][x] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            paths[a][b] = min(paths[a][b], paths[a][k] + paths[k][b])

MAX = 0
for path in paths:
    friends = 0
    for i in path:
        if 0 < i <= 2:
            friends += 1
    MAX = max(MAX, friends)
print(MAX)