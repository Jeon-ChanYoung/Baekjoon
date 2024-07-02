def power_sum(A, n):
    if n == 1:
        return A

    half_sum = power_sum(A, n//2) # S(A, n//2)
    x = multi(half_sum, add(identity(), pow(A, n//2))) # S(A, n//2) x (I + A^(n//2))

    if n%2 == 0:
        return x
    else:
        return add(x, pow(A, n))

def pow(A, n):
    if n == 1:
        return A
    x = pow(A, n//2)
    if n%2 == 0:
        return multi(x, x)
    else:
        return multi(multi(x, x), A)

def multi(A, B):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += A[i][k]*B[k][j]
                temp[i][j] %= 1000
    return temp

def add(A, B):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = A[i][j] + B[i][j]
    return temp

def identity():
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        temp[i][i] = 1
    return temp

N,B = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
result = power_sum(array, B)

for i in range(N):
    for j in range(N):
        print(result[i][j]%1000, end=" ")
    print()