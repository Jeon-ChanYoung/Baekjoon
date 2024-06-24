def solve():
    result = [[0] * M for _ in range(N)]
    for i in range(min(N,M)//2):
        result = simulation(result, i)
    return result

def simulation(result, i):
    temp = []
    temp += (array[i][i:M-i])
    temp += (array[y][M-i-1] for y in range(i+1, N-i-1))
    temp += (array[N-i-1][i:M-i][::-1])
    temp += (array[y][i] for y in range(N-i-2, i, -1))
    for _ in range(R % len(temp)): #rotate
        temp.append(temp.pop(0))

    index = 0
    for x in range(i, M-i):
        result[i][x] = temp[index]
        index += 1
    for y in range(i+1, N-i-1):
        result[y][M-i-1] = temp[index]
        index += 1
    for x in range(M-i-1, i-1, -1):
        result[N-i-1][x] = temp[index]
        index += 1
    for y in range(N-i-2, i, -1):
        result[y][i] = temp[index]
        index += 1
    return result

N,M,R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
array = solve()

for row in array:
    print(*row)