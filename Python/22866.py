N = int(input())
heights = list(map(int, input().split()))
number = [-1] * N
count = [0] * N
stack = []

for i in range(N):
    while stack and stack[-1][0] <= heights[i]:
        stack.pop()
    if stack:
        count[i] += len(stack)
        number[i] = stack[-1][1]
    stack.append([heights[i], i])

stack = []
for i in range(N-1, -1, -1):
    while stack and stack[-1][0] <= heights[i]:
        stack.pop()
    if stack:
        count[i] += len(stack)
        if number[i] == -1 or i - number[i] > stack[-1][1] - i:
            number[i] = stack[-1][1]
    stack.append([heights[i], i])

for cnt, num in zip(count, number):
    if cnt == 0:
        print(0)
    else:
        print(cnt, num+1)