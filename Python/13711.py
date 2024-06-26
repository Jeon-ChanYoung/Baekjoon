from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
info = {num : i for i,num in enumerate(A)}
array = [info[num] for num in B]
stack = [array[0]]

for i in range(1, N):
    if stack[-1] < array[i]:
        stack.append(array[i])
    else:
        stack[bisect_left(stack, array[i])] = array[i]
print(len(stack))