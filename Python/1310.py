import sys;input=sys.stdin.readline

def building_convex(point):
    lower = []
    upper = []
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

def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

N = int(input())
point = sorted([list(map(int, input().split())) for _ in range(N)])
convex_point = building_convex(point)
MAX = 0
k = 1

for i in range(len(convex_point)):
    while True:
        current_distance = distance(convex_point[i], convex_point[k])
        next_distance = distance(convex_point[i], convex_point[(k+1) % len(convex_point)])
        if next_distance <= current_distance:
            break
        k = (k + 1) % len(convex_point)
    MAX = max(MAX, current_distance)
print(MAX)