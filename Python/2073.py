D,P = map(int, input().split())
pipes = [list(map(int, input().split())) for _ in range(P)]
pipes.sort(key = lambda x:x[-1], reverse = True)
DP = [0] * (D+1)
DP[0] = 1

for length, volume in pipes:
    if DP[D - length] == 1:
        print(volume)
        break
    for i in range(D, length - 1, -1):
        DP[i] += DP[i - length] 
