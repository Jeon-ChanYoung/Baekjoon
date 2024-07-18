import sys;input=sys.stdin.readline

def CCW(pos1, pos2, pos3):
    x1, y1 = pos1
    x2, y2 = pos2
    x3, y3 = pos3
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)

def convex_hull(compare):
    stack = [position[0], position[1]]
    for pos in position[2:]:
        while len(stack) > 1 and compare(stack[-2], stack[-1], pos):
            stack.pop()
        if len(stack) < 2 or CCW(stack[-2], stack[-1], pos) != 0:
            stack.append(pos)
        elif CCW(stack[-2], stack[-1], pos) == 0:
            stack.pop()
            stack.append(pos)
    return stack

N = int(input())
position = sorted([tuple(map(int, input().split())) for _ in range(N)])
upper_hull = convex_hull(lambda p1, p2, p3 : CCW(p1, p2, p3) > 0)
lower_hull = convex_hull(lambda p1, p2, p3 : CCW(p1, p2, p3) < 0)
print(len(upper_hull) + len(lower_hull) - 2)

"""
from sys import stdin; input = stdin.readline

N = int(input())
points = []
for i in range (N):
    x, y = map(int, input().split())
    points.append((x, y))
points = sorted(points, key=lambda point: (point[0], point[1]))

def cross(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

lower = []
for p in points:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

upper = []
for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
        upper.pop()
    upper.append(p)

print(len(lower) + len(upper) - 2)
"""