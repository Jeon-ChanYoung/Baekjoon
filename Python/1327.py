from itertools import permutations
from collections import deque

N,K = map(int, input().split())
array = tuple(map(int, input().split()))
visit = [False] * 50000
arrayToNumber = {}

for i, case in enumerate(permutations(range(1, N+1))):
    arrayToNumber[case] = i

Q = deque([(array, 0)])
while Q:
    current, count = Q.popleft()
    if arrayToNumber[current] == 0:
        print(count)
        break

    for i in range(N - K + 1):
        new_current = list(current)
        new_current[i:i+K] = new_current[i:i+K][::-1]
        new_current = tuple(new_current)
        valid = arrayToNumber[new_current]
        if not visit[valid]:
            visit[valid] = True
            Q.append((new_current, count+1))
else:
    print(-1)
        