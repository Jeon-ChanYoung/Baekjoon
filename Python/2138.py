def solve(array):
    count = 0
    for i in range(N-1):
        if array[i] != target[i]:
            array[i] = 1 - array[i]
            array[i+1] = 1 - array[i+1]
            array[i+2] = 1 - array[i+2]
            count += 1

    if array[:-1] == target[:-1]:
        return count
    else:
        return 99999
    
N = int(input())
data = list(map(int, list(input()))) + [0]
target = list(map(int, list(input()))) + [0]

array1 = data[:]
array2 = data[:]
array2[0] = 1 - array2[0]
array2[1] = 1 - array2[1]

A = solve(array1)
B = solve(array2) + 1
result = min(A, B)
if result != 99999:
    print(result)
else:
    print(-1)