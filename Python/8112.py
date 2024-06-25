from collections import deque

for _ in range(int(input())):
    N = int(input())
    Q = deque([(1%N, "1")])
    visit = set()

    while Q:
        remainder, number = Q.popleft()
        
        if remainder == 0:
            print(number)
            break

        if remainder not in visit:
            visit.add(remainder)
            next_0 = (remainder * 10) % N
            next_1 = (remainder * 10 + 1) % N
            Q.append((next_0, number + "0"))
            Q.append((next_1, number + "1"))
    else:
        print("BRAK")