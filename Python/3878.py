def building_convex(points):
    if len(points) <= 1:
        return points
    lower = []
    for pos in points:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], pos) <= 2:
            lower.pop()
        lower.append(pos)
    upper = []
    for pos in reversed(points):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], pos) <= 2:
            upper.pop()
        upper.append(pos)
    return lower[:-1] + upper[:-1]

def CCW(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p1[1]*p2[0] + p2[1]*p3[0] + p3[1]*p1[0])

def checking_line(p1, p2, p3, p4):
    C1 = CCW(p1, p2, p3)
    C2 = CCW(p1, p2, p4)
    C3 = CCW(p3, p4, p1)
    C4 = CCW(p3, p4, p2)
    if C1*C2 <= 0 and C3*C4 <= 0:
        if C1*C2 != 0 and C3*C4 != 0:
            return True
        elif min(p1[0], p2[0]) <= max(p3[0], p4[0]) and \
             min(p1[1], p2[1]) <= max(p3[1], p4[1]) and \
             min(p3[0], p4[0]) <= max(p1[0], p2[0]) and \
             min(p3[1], p4[1]) <= max(p1[1], p2[1]):
             return True
    return False

def checking_hull(convex_point, inside):
    if len(convex_point) == 1:
        return False
    
    for inside_dot in inside:
        for i in range(len(convex_point)):
            p1 = convex_point[i]
            p2 = convex_point[(i+1) % len(convex_point)]
            p3 = inside_dot
            if CCW(p1, p2, p3) < 0:
                break
        else:
            return True
    return False

def check_intersection(convex1, convex2):
    for i in range(len(convex1)):
        p1 = convex1[i]
        p2 = convex1[(i + 1) % len(convex1)]
        for j in range(len(convex2)):
            p3 = convex2[j]
            p4 = convex2[(j + 1) % len(convex2)]
            if checking_line(p1, p2, p3, p4):
                return True
    return False

for _ in range(int(input())):
    N,M = map(int, input().split())
    blacks = sorted([list(map(int, input().split())) for _ in range(N)])
    whites = sorted([list(map(int, input().split())) for _ in range(M)])
    convex_blacks = building_convex(blacks)
    convex_whites = building_convex(whites)

    if len(convex_blacks) < 3 and len(convex_whites) < 3:
        p1 = convex_blacks[0]
        p2 = convex_blacks[1 % len(convex_blacks)]
        p3 = convex_whites[0]
        p4 = convex_whites[1 % len(convex_whites)]
        result = not checking_line(p1,p2,p3,p4) # 두 선분이 교차하면 True
    else:
        A = checking_hull(convex_blacks, convex_whites) # 집합내 다른 색깔이 존재한다면 True
        B = checking_hull(convex_whites, convex_blacks)
        C = check_intersection(convex_blacks, convex_whites) # 서로 다른 선분들 중 교차하는 선분이 있다면 True
        result = not (A or B or C)

    if result:
        print("YES")
    else:
        print("NO")