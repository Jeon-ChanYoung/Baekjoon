def power(n):
    if n == 1:
        return 2
    x = power(n//2)
    if n%2 == 0:
        return (x*x) % mod
    else:
        return (x*x*2) % mod

mod = 1_000_000_007

for _ in range(int(input())):
    N = int(input())
    if N < 3:
        print(1)
    else:
        print(int(power(N-2)))
