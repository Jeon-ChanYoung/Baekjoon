import sys;input=sys.stdin.readline
from math import ceil

def building_convex(point):
    lower=[]
    upper=[]
    for pos in point:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], pos) <= 0:
            lower.pop()
        lower.append(pos)
    for pos in reversed(point):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], pos) <= 0:
            upper.pop()
        upper.append(pos)
    return lower[:-1] + upper[:-1]

def CCW(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p1[1]*p2[0] + p2[1]*p3[0] + p3[1]*p1[0])

def distance(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3

    if x1 == x2: # 수직인 경우
        return abs(x3 - x1)
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1

    a = slope
    b = -1 
    c = intercept
    return abs(a*x3 + b*y3 + c) / (a**2 + b**2) ** 0.5    

num = 0
while True:
    N = int(input())
    if N == 0: break
    num += 1
    point = sorted([list(map(int, input().split())) for _ in range(N)])
    convex_point = building_convex(point)
    length = len(convex_point)
    MIN = 1e12

    for i in range(length):
        p1 = convex_point[i]
        p2 = convex_point[(i+1) % length]
        MAX = 0
        for j in range(length):
            p3 = convex_point[j]
            if p3 != p1 and p3 != p2:
                MAX = max(MAX, distance(p1, p2, p3))
        MIN = min(MIN, MAX)
    print(f'Case {num}: {ceil(MIN * 100) / 100:.2f}')