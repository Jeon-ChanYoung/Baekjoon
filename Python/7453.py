N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
AB_pair = {}
count = 0

for a in range(N):
    for b in range(N):
        total = array[a][0] + array[b][1]
        if total in AB_pair:
            AB_pair[total] += 1
        else:
            AB_pair[total] = 1

for c in range(N):
    for d in range(N):
        total = -(array[c][2] + array[d][3])
        if total in AB_pair:
            count += AB_pair[total]

print(count)
