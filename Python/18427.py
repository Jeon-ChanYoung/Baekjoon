N,M,H = map(int, input().split())
DP = [0] * (H+1)
DP[0] = 1

for _ in range(N):
    heights = list(map(int, input().split()))
    new_DP = DP[:]
    for height in heights:
        for i in range(H, height-1, -1):
            new_DP[i] = (new_DP[i] + DP[i - height]) % 10007
    DP = new_DP[:]

print(DP[H])