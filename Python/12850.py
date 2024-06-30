def multi(A, B):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += A[i][k]*B[k][j]
                temp[i][j] %= MOD
    return temp

def pow(graph, D):
    if D == 1:
        return graph
    x = pow(graph, D//2)
    if D%2 == 0:
        return multi(x, x)
    else:
        return multi(multi(x, x), graph)

n,m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

D = int(input())
MOD = 1_000_000_007

path = pow(graph, D)
print(path[0][0])