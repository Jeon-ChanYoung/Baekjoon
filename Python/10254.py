import sys;input=sys.stdin.readline

def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def CCW(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1) <= 0

def CCCW(p1, p2, p3, p4):
    temp = p4[:]
    temp[0] -= p3[0] - p2[0]
    temp[1] -= p3[1] - p2[1]
    return CCW(p1, p2, temp)

def building_convex(position):
    lower = []
    for pos in position:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], pos):
            lower.pop()
        lower.append(pos)
    upper = []
    for pos in reversed(position):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], pos):
            upper.pop()
        upper.append(pos)
    return lower[:-1] + upper[:-1]

def rotating_calipers(position):
    n = len(position)
    if n == 2:
        return position[0], position[1]
    max_dist = 0
    max_A, max_B = position[0], position[1]
    k = 1
    for i in range(n):
        while k+1 != i and not CCCW(position[i], position[(i+1)%n], position[k%n], position[(k+1)%n]):
            if distance(position[i], position[k%n]) > max_dist:
                max_dist = distance(position[i], position[k%n])
                max_A, max_B = position[i], position[k%n]
            k += 1
        if distance(position[i], position[k%n]) > max_dist:
            max_dist = distance(position[i], position[k%n])
            max_A, max_B = position[i], position[k%n]
    return max_A, max_B

for _ in range(int(input())):
    N = int(input())
    position = sorted([list(map(int, input().split())) for _ in range(N)])
    convex_position = building_convex(position)
    result = rotating_calipers(convex_position)
    print(*result[0], *result[1])