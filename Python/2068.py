def multi(A, B):
    x1 = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod
    x2 = (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod
    x3 = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod
    x4 = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod
    return [[x1, x2],
            [x3, x4]]

def power(A, n):
    if n == 1:
        return A
    x = power(A, n//2)
    if n%2 == 0:
        return multi(x, x)
    else:
        return multi(multi(x, x), A)

a,b = map(int, input().split())
mod = 1_000_000_000

A = [[1,1],
     [1,0]]

result_A = power(A,a)
result_B = power(A,b+1)
result = result_B[0][0] - result_A[0][0]

if result < 0:
    print(mod + result)
else:
    print(result)