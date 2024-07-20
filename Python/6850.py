import sys;input=sys.stdin.readline

def CCW(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)

N = int(input())
position = [list(map(int, input().split())) for _ in range(N)]
position.sort(key=lambda x:(x[0], x[1]))

lower = []
for pos in position:
    while len(lower) >= 2 and CCW(lower[-2], lower[-1], pos) >= 0:
        lower.pop()
    lower.append(pos)

upper = []
for pos in reversed(position):
    while len(upper) >= 2 and CCW(upper[-2], upper[-1], pos) >= 0:
        upper.pop()
    upper.append(pos)

result = lower[:-1] + upper[:-1]
if len(result) < 3:
    print(0)
else: 
    xPos = [x for x,_ in result] + [result[0][0]]
    yPos = [y for _,y in result] + [result[0][1]]
    area = 0

    for i in range(len(result)):
        area += xPos[i] * yPos[i+1]

    for i in range(len(result)):
        area -= yPos[i] * xPos[i+1]
    print(abs(area) // 100)