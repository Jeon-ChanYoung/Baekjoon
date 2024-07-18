import sys;input=sys.stdin.readline

def CCW(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)

for _ in range(int(input())):
    N = int(input())
    temp = []
    for _ in range((N-1)//5 + 1):
        temp += list(map(int, input().split()))
    position = [(x,y) for x,y in zip(temp[::2], temp[1::2])]
    position.sort(key=lambda x : (-x[1], x[0]))

    upper = []
    for pos in position:
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], pos) >= 0:
            upper.pop()
        upper.append(pos)

    lower = []
    for pos in reversed(position):
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], pos) >= 0:
            lower.pop()
        lower.append(pos)

    print(len(upper) + len(lower) - 2)
    for pos in upper[:-1]:
        print(*pos)

    for pos in lower[:-1]:
        print(*pos)
