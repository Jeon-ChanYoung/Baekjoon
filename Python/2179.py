import sys
input = lambda : sys.stdin.readline().strip()

def partial_Length(word1, word2):
    if word1 == word2:
        return 0

    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            return i
    return i+1

N = int(input())
words = [input() for _ in range(N)]
sorted_words = sorted(words)
info = []
maxLength_list = set()
maxLength = 0

for i in range(N-1):
    word1 = sorted_words[i]
    word2 = sorted_words[i+1]
    length = partial_Length(word1, word2)
    maxLength = max(maxLength, length)
    info.append((length, word1, word2))

for length, word1, word2 in info:
    if length == maxLength:
        maxLength_list.update({word1, word2})

for word in words:
    if word in maxLength_list:
        target = word
        print(word)
        break

for word in words:
    if partial_Length(word, target) == maxLength:
        print(word)
        break