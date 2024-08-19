import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, depth):
    global count, visit

    isLeaf = True
    for next in graph[node]:
        if not visit[next]:
            visit[next] = True
            dfs(next, depth+1)
            isLeaf = False
    if isLeaf:
        count += depth
    
N = int(input())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
visit[1] = True
count = 0

for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)
print(["No", "Yes"][count%2])