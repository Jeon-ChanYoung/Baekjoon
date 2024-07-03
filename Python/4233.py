def isPrime(p):
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

def power(a, p):
    if p == 1:
        return a
    x = power(a, p//2)
    if p%2 == 0:
        return (x*x) % mod
    else:
        return (x*x*a) % mod

for input in iter(input, "0 0"):
    p,a = map(int, input.split())
    mod = p

    if not isPrime(p) and power(a, p) == a:
        print("yes")
    else:
        print("no")