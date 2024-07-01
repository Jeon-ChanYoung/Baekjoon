def multi(A, B):
    x1 = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD
    x2 = (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD
    x3 = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD
    x4 = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD
    return [[x1,x2],[x3,x4]]

def pow(A, n):
    if n == 1:
        return A
    x = pow(A, n//2)
    if n%2 == 0:
        return multi(x,x)
    else:
        return multi(multi(x,x),A)

n = int(input())
A = [[1,1],[1,0]]
MOD = 1_000_000_007
matrix = pow(A, n)
result = (matrix[0][0] ** 2 - matrix[0][1] ** 2) % MOD
 
if n%2 == 0:
    result -= 1
else:
    result += 1

if result < 0:
    print(MOD + result)
else:
    print(result)