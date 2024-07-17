import sys;input=sys.stdin.readline
from heapq import *

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
distance = [float('inf')] * (N+1)
distance[1] = 0 

for i in range(M):
    A,B = map(int, input().split())
    graph[A].append((B, i+1))
    graph[B].append((A, i+1))

Q = []
heappush(Q, (1, 1))

while Q:
    current, node = heappop(Q)
    visit[node] = True

    for next_node, number in graph[node]:
        if visit[next_node]:
            continue

        time = (number - current % M + M) % M
        if distance[next_node] > time + current:
            distance[next_node] = time + current
            heappush(Q, (time + current, next_node))

print(distance[-1])