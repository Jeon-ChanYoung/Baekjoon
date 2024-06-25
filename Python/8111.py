from collections import deque

for _ in range(int(input())):
    N = int(input())
    Q = deque(["1"])
    visit = set()

    while Q:
        number = Q.popleft()
        if int(number) % N == 0:
            print(number)
            break
        
        R = int(number) % N
        if len(number) <= 100 and R not in visit:
            visit.add(R)
            Q.append(number + "0")
            Q.append(number + "1")
    else:
        print("BRAK")