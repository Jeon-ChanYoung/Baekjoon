word = input()
length = len(word)
isPalind = [[0] * length for _ in range(length)]
DP = [99999] * (length+1)
DP[0] = 0

for i in range(length):
    isPalind[i][i] = 1

for i in range(length-1):
    if word[i] == word[i+1]:
        isPalind[i][i+1] = 1

for i in range(3, length+1):
    for j in range(length - i + 1):
        left = j
        right = j + i - 1
        if isPalind[left+1][right-1] and word[left] == word[right]:
            isPalind[left][right] = 1

for right in range(1, length+1):
    for left in range(1, right+1):
        if isPalind[left-1][right-1]:
            DP[right] = min(DP[right], DP[left-1] + 1)
print(DP[-1])