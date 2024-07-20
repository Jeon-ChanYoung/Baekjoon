import sys;input=sys.stdin.readline

def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def CCW(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)

def building_convex(position):
    lower = []
    for pos in position:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], pos) <= 0:
            lower.pop()
        lower.append(pos)
    upper = []
    for pos in reversed(position):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], pos) <= 0:
            upper.pop()
        upper.append(pos)
    return lower[:-1] + upper[:-1]

def rotating_calipers(position):
    length = len(position)
    if length == 2:
        return distance(position[0], position[1])
    MAX = 0
    k = 1
    for i in range(length):
        while True:
            current_distance = distance(position[i], position[k])
            next_distance = distance(position[i], position[(k+1) % length])
            if next_distance <= current_distance:
                break
            k = (k+1) % length
        MAX = max(MAX, distance(position[i], position[k]))
    return MAX

N = int(input())
position = sorted([list(map(int, input().split())) for _ in range(N)])
convex_position = building_convex(position)
result = rotating_calipers(convex_position)
print(result)