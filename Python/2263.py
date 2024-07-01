import sys;sys.setrecursionlimit(10**6)

def solve(In_start, In_end, post_start, post_end):
    if In_start > In_end or post_start > post_end:
        return 
    
    root = postorder[post_end]
    left = nodeIndex[root] - In_start
    right = In_end - nodeIndex[root]
    print(root, end=" ")
    solve(In_start, In_start+left-1, post_start, post_start+left-1)
    solve(In_end-right+1, In_end, post_end-right, post_end-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
nodeIndex = [0] * (n + 1)

for index in range(n):
    nodeIndex[inorder[index]] = index

solve(0, n-1, 0, n-1)
