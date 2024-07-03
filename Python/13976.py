def power(matrix, n):
    if n == 1:
        return matrix
    x = power(matrix, n//2)
    if n%2 == 0:
        return multi(x, x)
    else:
        return multi(multi(x, x), matrix)
        
def multi(A, B):
    x1 = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD
    x2 = (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD
    x3 = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD
    x4 = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD
    return [[x1,x2], [x3,x4]]

N = int(input())
MOD = 1_000_000_007

if N%2 != 0:
    print(0)
else:
    N //= 2
    matrix = [[4,-1], [1,0]] # f(x) = 4f(x-1) - f(x-2)
    matrix_pow = power(matrix, N)
    result = matrix_pow[0][0] - matrix_pow[1][0]
    print((MOD + result) % MOD)
