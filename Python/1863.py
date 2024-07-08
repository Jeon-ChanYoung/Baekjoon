import sys;input=sys.stdin.readline

N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
pos.sort()
stack = [[0,0]]
count = 0

for x,y in pos:
    if stack[-1][1] < y:
        count += 1
        stack.append([x,y])
    else:
        while stack[-1][1] > y:
            stack.pop()
        if stack[-1][1] < y:
            count += 1
            stack.append([x,y])
print(count)