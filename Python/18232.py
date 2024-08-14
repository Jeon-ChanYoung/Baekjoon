import sys
from collections import deque
input = lambda : map(int, sys.stdin.readline().split())

N,M = input()
S,E = input()
teleport = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = input()
    teleport[x].append(y)
    teleport[y].append(x)

visit = [False] * (N+1)
visit[S] = True
Q = deque([(S,0)])
while Q:
    x, count = Q.popleft()
    if x == E:
        print(count)
        break

    for X in [x-1, x+1, *teleport[x]]:
        if 0<X<=N and not visit[X]:
            visit[X] = True
            Q.append((X,count+1))