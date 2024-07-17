import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    x = power(a, n // 2)
    if n % 2 == 0:
        return (x * x) % MOD
    else:
        return (x * x * a) % MOD

MOD = 1_000_000_007
total = 0
for _ in range(int(input())):
    C, K = map(int, input().split())
    if K != 0:
        total += C * K * power(2, K-1)
print(total % MOD)
