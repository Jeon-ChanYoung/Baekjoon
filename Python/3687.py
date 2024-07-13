MIN = [0,0] # 0~1
MIN.extend([1,7,4,2,6,8,10]) # 2~8
MIN.extend([18,22,20,28,68,88,108]) # 9~15
MIN.extend([188,200,208,288,688]) # 16~20`

for _ in range(int(input())):
    N = int(input())
    answer = [] 
    if N < 18:
        answer.append(MIN[N])
    else:
        answer.append(str(MIN[N%7+14]) + (N-14)//7 * "8")
        
    if N % 2 == 0:
        answer.append("1" * (N//2))
    else:
        answer.append("7"+"1"*(N//2 - 1))

    print(*answer)