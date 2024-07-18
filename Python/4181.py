import sys;input=sys.stdin.readline

def CCW(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)

N = int(input())
position = []
for _ in range(N):
    x,y = map(int, input()[:-2].split())
    position.append((x,y))
position.sort(key=lambda x:(x[0], x[1]))

lower = []
for pos in position:
    while len(lower) >= 2 and CCW(lower[-2], lower[-1], pos) < 0:
        lower.pop()
    lower.append(pos)

upper = []
for pos in reversed(position):
    while len(upper) >= 2 and CCW(upper[-2], upper[-1], pos) < 0:
        upper.pop()
    upper.append(pos)

result = lower[:-1] + upper[:-1]
print(len(result))
for pos in result:
    print(*pos)