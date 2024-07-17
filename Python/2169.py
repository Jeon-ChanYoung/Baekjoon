N,M = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

for x in range(M-1):
    land[0][x+1] += land[0][x]

for y in range(1, N):
    land1 = land[y][:]
    land2 = land[y][:]
    land1[0] += land[y-1][0]
    land2[M-1] += land[y-1][M-1]

    for x in range(M-1):
        land1[x+1] += max(land1[x], land[y-1][x+1]) 
        land2[M-x-2] += max(land2[M-x-1], land[y-1][M-x-2]) 

    for x in range(M):
        land[y][x] = max(land1[x], land2[x])

print(land[-1][-1])