for _ in range(int(input())):
    N = int(input())
    answer = [0,0,0,0,0]
    answer[0] = N // 60
    N %= 60

    if N > 35:
        answer[0] += 1
        answer[2] = (64 - N) // 10 
        if 5 <= N%10:
            answer[4] = 10 - N%10
        else:
            answer[3] = N%10

    else:
        answer[1] = (N+4) // 10
        if 5 < N%10:
            answer[4] = 10 - N%10
        else:
            answer[3] = N%10

    print(*answer)