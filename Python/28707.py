from heapq import *

def isSorted(arr):
    for i in range(N-1):
        if arr[i] > arr[i+1]:
            return False
    return True

N = int(input())
array = list(map(int,input().split()))
M = int(input())
LRC = [list(map(int, input().split())) for _ in range(M)]
visit = set()
Q = [[0, tuple(array)]]

while Q:
    distance, arr = heappop(Q)
    if arr in visit:
        continue
    visit.add(arr)
    if isSorted(arr):
        print(distance)
        break
    for l,r,c in LRC:
        new_arr = list(arr[:])
        new_arr[l-1], new_arr[r-1] = new_arr[r-1], new_arr[l-1]
        heappush(Q, [distance+c, tuple(new_arr)])
else:
    print(-1)