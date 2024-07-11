N,A,B = map(int, input().split())
answer = []

if N < A + B - 1:
    print(-1)
    exit()

if A >= B:
    for i in range(1, A+1):
        answer.append(i)

    for i in range(B-1, 0, -1):
        answer.append(i)
else:
    for i in range(1, A):
        answer.append(i)
    
    for i in range(B, 0, -1):
        answer.append(i)

answer.insert(1, " ".join(list("1"*(N - A - B + 1))))
for num in answer:
    if num:
        print(num, end = " ")