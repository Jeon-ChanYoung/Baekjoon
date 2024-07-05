def minmax(array):
    global MIN, MAX

    for i in range(len(array) - K + 1):
        gap = array[i+K-1] - array[i]
        MIN = min(MIN, gap+1)
        MAX = max(MAX, gap+1)

for _ in range(int(input())):
    W = input()
    K = int(input())
    alphabet = {}
    MIN = 99999
    MAX = 0

    # abaaaba -> {'a': [0, 2, 3, 4, 6], 'b': [1, 5]}
    for index, alpha in enumerate(W):
        if alpha not in alphabet:
            alphabet[alpha] = [(index)]
        else:
            alphabet[alpha].append(index)

    for array in alphabet.values():
        if len(array) >= K:
            minmax(array)

    if MAX == 0:
        print(-1)
    else:
        print(MIN, MAX)