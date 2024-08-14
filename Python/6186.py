R,C = map(int, input().split())
grass = [["."]*(C+2)] + ["."+input()+"." for _ in range(R)] + [["."]*(C+2)]
visit = [[False]*(C+2) for _ in range(R+2)]
count = 0

for y in range(1, R+1):
    for x in range(1, C+1):
        if not visit[y][x] and grass[y][x] == "#":
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                X = x+dx
                Y = y+dy
                if grass[Y][X] == "#":
                    visit[y][x] = visit[Y][X] = True
                    count += 1
                    break
            else:
                visit[y][x] = True
                count += 1
print(count)

