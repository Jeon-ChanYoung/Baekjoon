import sys;input=sys.stdin.readline

def g(a,n):
    if n==1:
        return a 
    x=g(a,n//2)
    if n%2==0:
        return (x*x)%P
    else:
        return (x*x*a)%P

P=1_000_000_007
f = [0] * 4_000_001
f[0] = 1
for i in range(1, len(f)):
    f[i] = (f[i-1]*i)%P

for _ in range(int(input())):
    N,K=map(int,input().split())
    print(f[N] * g(f[N-K] * f[K], P-2) % P)
