from functools import cmp_to_key

def CCW(p1, p2, p3):
    x1,y1,_ = p1
    x2,y2,_ = p2
    x3,y3,_ = p3
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)

def cmp(p1,p2):
    return CCW(point, p1, p2)

for _ in range(int(input())):
    temp = list(map(int, input().split()))
    position = []
    for i in range(temp[0]):
        x = temp[2*i+1]
        y = temp[2*i+2]
        position.append((x,y,i))
    position.sort(key = lambda x:(x[0], x[1]))
    point = position[0]
    position = [point] + sorted(position[1:], key=cmp_to_key(cmp))

    k = 0
    while True:
        p1 = position[k]
        p2 = position[k-1]
        p3 = position[k-2]
        if CCW(p1, p2, p3) != 0:
            break
        k -= 1

    position = position[:k-1] + position[:k-2:-1]
    result = [num for x,y,num in position]
    print(*result)
