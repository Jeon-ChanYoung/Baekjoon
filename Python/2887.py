import sys;input=sys.stdin.readline

def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def union(A, B):
    root_A = find(A)
    root_B = find(B)
    parent[max(root_A, root_B)] = min(root_A, root_B)

N = int(input())
pos = [list(map(int, input().split())) + [i] for i in range(N)]
edges = []
price = 0
parent = list(range(N+1))

for i in range(3):
    pos.sort(key=lambda x:x[i])
    for j in range(N-1):
        A = pos[j]
        B = pos[j+1]
        edges.append([abs(A[i] - B[i]), A[3], B[3]])

edges.sort()
for weight, A, B in edges:
    if find(A) != find(B):
        union(A, B)
        price += weight

print(price)