N = int(input())
DP = [[[0] * (1<<10) for _ in range(10)] for _ in range(101)]
mod = 1_000_000_000

for i in range(1, 10):
    DP[0][i][1<<i] = 1

for i in range(100):
    for k in range(1<<10):
        DP[i+1][0][k|(1<<0)] += DP[i][1][k] % mod
        DP[i+1][9][k|(1<<9)] += DP[i][8][k] % mod
        for j in range(1, 9):
            DP[i+1][j][k|(1<<j)] += (DP[i][j-1][k] + DP[i][j+1][k]) % mod

total = 0
for i in range(10):
    total += DP[N-1][i][1023] % mod
print(total % mod)