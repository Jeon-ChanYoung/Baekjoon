def reversePrice(floor):
    A = str(floor).zfill(K) # 두자리일 때 : 2 -> 02 
    B = str(X).zfill(K)
    total = 0

    for a, b in zip(A, B):
        total += price[int(a)][int(b)]
    return total

N,K,P,X = map(int, input().split())
count = 0
price = [[0,4,3,3,4,3,2,3,1,2],
         [4,0,5,3,2,5,6,1,5,4],
         [3,5,0,2,5,4,3,4,2,3],
         [3,3,2,0,3,2,3,2,2,1],
         [4,2,5,3,0,3,4,3,3,2],
         [3,5,4,2,3,0,1,4,2,1],
         [2,6,3,3,4,1,0,5,1,2],
         [3,1,4,2,3,4,5,0,4,3],
         [1,5,2,2,3,2,1,4,0,1],
         [2,4,3,1,2,1,2,3,1,0]]

for floor in range(1, N+1):
    if reversePrice(floor) <= P:
        count += 1
print(count-1)