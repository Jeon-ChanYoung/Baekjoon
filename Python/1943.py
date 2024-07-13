def solve():
    N = int(input())
    coins = [list(map(int, input().split())) for _ in range(N)]
    target = sum(weight * count for weight, count in coins)

    if target % 2 != 0:
        return False
    
    target //= 2
    DP = [False] * (target + 1)
    DP[0] = True

    for weight, count in coins:
        for i in range(target, weight-1, -1):
            if DP[i - weight]:
                for j in range(count):
                    next_index = i + weight * j
                    if 0 <= next_index <= target:
                        DP[next_index] = True
    return DP[target]

for _ in range(3):
    result = solve()
    if result:
        print(1)
    else:
        print(0)