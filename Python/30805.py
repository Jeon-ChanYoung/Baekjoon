def find(array, value, start):
    try:
        sliced_index = array[start:].index(value)
        return start + sliced_index
    except:
        return -1

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

descending_array = sorted(A, reverse=True)
partial_sequence = []

A_startIndex = 0
B_startIndex = 0
for element in descending_array:
    A_index = find(A, element, A_startIndex)
    B_index = find(B, element, B_startIndex)
    if A_index != -1 and B_index != -1:
        partial_sequence.append(element)
        A_startIndex = A_index + 1
        B_startIndex = B_index + 1

print(len(partial_sequence))     
print(*partial_sequence)

