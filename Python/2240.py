T, W = map(int, input().split())
plums = [int(input()) - 1 for _ in range(T)]
DP = [0]*(W+1)

for w in range(plums[0], W + 1, 2):
    DP[w] = 1

for t in range(1, T):
    new_DP = DP[:]
    new_DP[0] = DP[0] + (plums[t] == 0)
    for w in range(1, W + 1) :
        new_DP[w] = max(DP[w], DP[w-1]) + (w%2 == plums[t])
    DP = new_DP
print(max(DP))