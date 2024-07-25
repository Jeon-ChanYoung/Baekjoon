def main():
    N, Px, Py = map(int, input().split())
    count = 0
    prison_pos = [Px, Py]
    points = [list(map(int, input().split())) for _ in range(N)]

    while len(points) >= 3:
        points = sorted(points)
        convex_hull = build_convex_hull(points)
        if not is_point_in_convex_hull(prison_pos, convex_hull):
            break

        count += 1
        points = remove_points(points, convex_hull)

    print(count)


def is_point_in_convex_hull(point, convex_hull):
    directions = []
    for i in range(len(convex_hull)):
        p1 = convex_hull[i]
        p2 = convex_hull[(i + 1) % len(convex_hull)]
        directions.append(ccw(p1, p2, point))

    first_direction = directions[0]
    return all(d * first_direction >= 0 for d in directions)


def build_convex_hull(points):
    lower = []
    upper = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def remove_points(points, points_to_remove):
    return [p for p in points if p not in points_to_remove]

main()
