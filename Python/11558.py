import sys;input=sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    D = {}

    for i in range(1, N+1):
        number = int(input())
        D[i] = number

    number = 1
    for i in range(N+1):
        if number == N:
            print(i)
            break
        number = D[number]
    else:
        print(0)
