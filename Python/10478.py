for N in iter(input, "0"):
    N = int(N)
    units = {unit:i for i,unit in enumerate(input().split())}
    matrix = [[float('inf')]*N for _ in range(N)]

    for _ in range(N-1):
        a, _, num, b = input().split()
        a = units[a]
        b = units[b]
        num = int(num)
        matrix[a][b] = num
        matrix[b][a] = 1/num

    for k in range(N):
        for a in range(N):
            for b in range(N):
                matrix[a][b] = min(matrix[a][b], matrix[a][k]*matrix[k][b])

    for i in range(N):
        matrix[i][i] = 1

    index = matrix[0].index(min(matrix[0]))
    array = sorted([(num, unit) for num, unit in zip(matrix[index], units.keys())])
    answer = [f"{int(num+0.5)}{unit}" for num, unit in array]
    print(" = ".join(answer))
