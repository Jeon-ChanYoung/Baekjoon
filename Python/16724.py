def simulation(x, y, number):
    if parent[y][x] == number or parent[y][x] != 0:
        return parent[y][x]
    
    parent[y][x] = number
    d = info[y][x]

    if d == "U":
        parent[y][x] = simulation(x, y-1, number)
    elif d == "R":
        parent[y][x] = simulation(x+1, y, number)
    elif d == "D":
        parent[y][x] = simulation(x, y+1, number)
    else:
        parent[y][x] = simulation(x-1, y, number)
    return parent[y][x]

N,M = map(int,input().split())
info = [input() for _ in range(N)]
parent = [[0] * M for _ in range(N)]
number = 1
count = set()

for y in range(N):
    for x in range(M):
        if parent[y][x] == 0:
            simulation(x, y, number)
            number += 1
            
for y in range(N):
    for x in range(M):
        count.add(parent[y][x])
print(len(count))