import sys;input=sys.stdin.readline
from bisect import bisect_left

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

pos = [0] * N
pos[0] = 1
stack = [lines[0][1]]

for i in range(1, N):
    if stack[-1] < lines[i][1]:
        stack.append(lines[i][1])
        pos[i] = len(stack)
    else:
        index = bisect_left(stack, lines[i][1])
        stack[index] = lines[i][1]
        pos[i] = index+1

value = max(pos)
answer = [False] * 500001
for i in range(N-1, -1, -1): 
    if pos[i] != value:
        answer[i] = True
    else:
        value -= 1

print(sum(answer))
for i in range(N):
    if answer[i]:
        print(lines[i][0])