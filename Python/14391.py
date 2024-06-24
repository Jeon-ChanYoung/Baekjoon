def mapping(slice):
    temp = []
    for i in range(N):
        temp.append(list(map(int, list(slice[M*i : M*(i+1)]))))
    return temp

def calculation(paperCase):
    total = 0
    visit = [[False]*M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if not visit[y][x]:
                direction = paperCase[y][x]         #0 -> 가로
                total += piece(x,y,direction,visit) #1 -> 세로
    return total

def piece(x, y, direction, visit):
    total = ""
    while True:
        total += paper[y][x]
        visit[y][x] = True
        if direction == 0 and x+1 < M and paperCase[y][x+1] == 0:
            x += 1
        elif direction == 1 and y+1 < N and paperCase[y+1][x] == 1:
            y += 1
        else:
            return int(total)

N,M = map(int, input().split())
paper = [input() for _ in range(N)]
MAX = 0

for i in range(2 ** (N*M)):
    slice = bin(i)[2:].zfill(N*M) # 1 -> 000001 이진수로 변환
    paperCase = mapping(slice)    # 000001 -> [[0, 0, 0], [0, 0, 1]]
    total = calculation(paperCase)
    MAX = max(MAX, total)

print(MAX)